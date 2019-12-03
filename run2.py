# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:20:15 2019

@author: Anna
"""

import pandas as pd
import resistances2 as rs
import numpy as np
import gsto
import cO3
import flux2 as fl
import configure
# cd C:\Users\anuri\Documents\PODY_py_software_LIST\OzoneDeposition-RUN2

###########################################################################################
data = pd.read_excel(configure.input_data_file)

### Determinig factor functions "f" from UNECE Mapping critical leveks for vegetation - chapter III
# Phenology
fphen_y = gsto.fphen_year(365)  # year with 365 days

# Light condition
fleaf_light = data["R (Wh/m^2)"].apply(gsto.fleaf_light) 

# Water condition, Vapour pressure deficit
VPD = gsto.VPD(data["_RH%"], gsto.SVP(data["Ts_C (C)"])) #### APLIKUJ NAJPRV RH_per, potom Teplotu
fVPD = VPD.apply(gsto.fVPD)
#vfVPDF = np.vectorize(gsto.fVPD)
#fVPD = vfVPDF(VPD)
#fVPD = pd.Series(fVPD)

ftemp = data["Ts_C (C)"].apply(gsto.ftemp)

# External conductance
gext = 1/ rs.static_param("rext")

# Stomatal conductance
gstol = gsto.gstol(fphen_y, fleaf_light, fVPD, ftemp)


# Friction velocity u* for futher calculations
vu_starF = np.vectorize(rs.u_star)      # vectorised function u*
vu_star = vu_starF(data["uh_zR (m/s)"])
vu_star = pd.Series(vu_star)

# In-canopy resistance
Rinc = rs.Rinc(rs.SAI(rs.LAI()),vu_star)
#Rinc = rs.Rinc(LAI.SAI,vu_star(data["uh_zR (m/s)"]))

# Stomatal resistance
vrstolF = np.vectorize(rs.rstol)   #  vectorised stomatal resistance
vrstol = pd.Series(vrstolF(gstol))

# Surface resistance
#Rsur = rs.Rsur(rs.LAI(), vrstol , Rinc)
Rsur = 1 / (rs.LAI() / vrstol + (1 + rs.LAI())/rs.static_param("rext") + 1/(Rinc + rs.static_param("Rsoil")))
#problem, teraz je LAI array, preto Rsur nevie ktore z LAI pouzit...
#teraz rieš ine...

# Ozone concentration
cO3_nmolm3 = cO3.cO3_nmolm3(data["O3_zR (ppb)"], data["P (kPa)"], data["Ts_C (C)"])

# Stomatal flux
Fst_l = fl.Fstl(cO3_nmolm3, Rsur, rs.Rb(data["uh_zR (m/s)"]), gstol)

# Phytotoxic ozone dose
POD0, POD1 = 0, 0
for i in range(1,8760):
    POD0 = Fst_l[i]*0.0036 + POD0
    if Fst_l[i] > 1:
            POD1 = 0.0036*(Fst_l[i]-1)+POD1

print("POD0 = ", POD0)
print("POD1 = ", POD1)
            #print("Fst_l = ", Fst_l)