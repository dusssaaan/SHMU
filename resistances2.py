# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:20:48 2019

@author: Anna 
"""

#import numpy as np
import pandas as pd
import math
import numpy as np
import configure



static_df = pd.read_csv(configure.static_params_file, delimiter=";", decimal = ",", header = [0])

static_param_d=dict(zip(static_df[static_df.columns[0]], static_df[static_df.columns[1]]))

def static_param(x):
    return static_param_d[x];

"""
# DICTIONARY UPLOADING
def static_param(x,static_params_file=static_params_file):    #adres = "C:/Users/anuri/Documents/InputData/Dictionary.csv" # pre mini noťas
  
    temp = pd.read_csv(static_params_file, delimiter=";", decimal = ",", header = [0])
    #dataset = pd.read_csv("C:/Users/anuri/Documents/InputData/Dictionary.csv", delimiter=";", decimal = ",", header = [0])
    # decimal = "," # v povodnom dokumente oznacujeme desatinnu ciarku ciarkou, robilo to šarapatu
    # teraz uz nebude treba menit string na float, lebo uz cisla rozpozna ako cisla
    dataDict = temp.loc[:,["Name","Value"]]
    dic = dataDict.set_index('Name')['Value'].to_dict()
    for key, val in dic.items():
        if key == x:
            return float(val)
"""
    
# cd \Documents\PODY_py_software_LIST\OzoneDeposition-RUN2
#data_dict = ul.dict_upload("C:/Users/anuri/Documents/InputData/Dictionary.csv")

def u_star(u):            # u - single hodnota
    """Friction velocity 
    Simpson et al. 2012
    [m s-1] minimal value of u_* is 0.03732. For our parametrisation:"""
    if (u == 0):
        temp = static_param("k")/(math.log(3, math.e)*10)
    else:
        temp = u * static_param("k") / math.log(3, math.e)    
    #temp = temp.replace(0,k/(math.log(3, math.e)*10)) # lebo ak u = 0, tak u* = 0.03732.... a nie 0 ako nám vychádza podľa vzorca 
    return temp


def vu_star():    
    vu_starF = np.vectorize(u_star)
#    vu_starF = pd.Series(vu_starF(u))
#    vu_star = vu_starF(data["uh_zR (m/s)"])
    return vu_starF

def Rb(u_star):             # input - single value, np.array, pd.Series
    """Quasi-laminar resistance
    Simpson et al. 2012: EMEP MSC-W model: description, eq. 53, Simpson 2003
    Sc is Schmidt number, Pr is Prandtl number, Di is diffusivity of ozone (Massman 1998)"""
    temp = 2 / (static_param("k") * u_star) *(static_param("Sc") *10**4/ static_param("Di") * 0.72)** (2/3)
    # Ked bude v dictionary Pr= 0.72 a Di = 0.15. Dovtedy povodne.  
    #temp = 2 / (k * u_star) *(data_dict["Sc"] *10**4/ (data_dict["Di"] * 0.72))** (2/3)
    return temp

def Rinc(SAI, u_star):  # input - single value, np.array, pd.Series
    """In-canopy resistance
    Erisman et al. 1974
    [s m-1]""" #lit. je v Simpson 2012, str. 7846
    temp = 14 * SAI * 20 / u_star
    return temp

def apply_max(index):   # input - pd.Series
    return max(static_param("fmin"), index)

def apply_min(index):   # input - pd.Series
    return min(1, index)

def gstol(fphen, fleaf_light, fVPD, ftemp): # input iba pd.Series!!! 
    """Based od Jarvis 1976 - The interpretation of the variations in leaf water potential and stomatal conductance found in canopies in the field.
    and improved by Emberson 2000, Simpson et al. 2012, CLRTAP 2017 (chap 3, pg 17)
    gstol and gmax [mmol O3 m-2 PLA s-1]"""
    #temp = static_param("gmax") * fphen * fleaf_light * (ftemp * fVPD).apply(apply_max)#  max(fmin, ftemp * fVDP)
    temp = (ftemp * fVPD).apply(apply_max) * static_param("gmax") * fphen * fleaf_light #  max(fmin, ftemp * fVDP)
    return temp

def rstol(gstol):   # input single value
    """ Stomatal resistance is reciprocal stomatal conductance, unit conversion is by conversion factor 41000.
    Maximal value of stomatal resistance is 100000. 
    [s m-1]"""   
    if gstol == 0:
        temp = 100000
    else:
        temp = 41000 / gstol
    return temp

def Rsur(LAIt, rstol,  Rinc):   # input single value
    """Surface resistance to ozone deposition , it comprises of resistance of plant canopy and undeelying soil.
    Emberson 2001 Modelling and mapping ozone deposition in Europe
    [s m-1]
    rext is the external resistance of the exterior plant parts, Rinc is the land-cover specific in-canooy aerodynamic resistance,
    Rsoil = Rgs is the soil resistance to destruction or absorption at the ground surface"""
#    temp = 1 / (LAIt / rstol + (1 + LAIt)/static_param("rext") + 1/(Rinc + static_param("Rsoil")))
    temp = 1 / (LAIt / rstol + (1 + LAIt)/static_param("rext") + 1/(Rinc + static_param("Rsoil")))
    return temp
#1 / (rs.LAI() / vrstol + (1 + rs.LAI())/rs.static_param("rext") + 1/(Rinc + rs.static_param("Rsoil")))

#    if LAIt == static_param("LAI_a") or LAIt == static_param("LAI_d"):
#       SAI = LAIt
#    else:
#        SAI = LAIt + 1

def LAI():
    """ Leaf area index 
    Simpson 2003 - skontroluj"""
    r = np.arange(1,366,1)
    SGS, EGS = int(static_param("Astart_FD")), int(static_param("Aend_FD"))
    LAIp_a, LAIp_b = int(static_param("LAI_1")), int(static_param("LAI_2"))
    LAI_a, LAI_b, LAI_c, LAI_d = static_param("LAI_a"), static_param("LAI_b"), static_param("LAI_c"), static_param("LAI_d")

    # LAI parameters LAI_a - LAI_2 set up according Simpson 2003         (NESEDI DOKONALE!!..)
    LAI = np.full(365,np.NaN)

    LAI[:SGS - 1]=LAI_a
    for i in range(LAIp_a + 1):
        LAI[SGS + i - 1] = ((LAI_b-LAI_a)*i/LAIp_a+LAI_a)
    #print('LAI = ', LAI[SGS+i])

    for i in range(EGS - SGS - LAIp_a - LAIp_b + 1):
        LAI[SGS + LAIp_a + i - 1] = LAI_b +(LAI_c-LAI_b)*i/(EGS - SGS - LAIp_a - LAIp_b)
    #print('LAI = ', LAI[SGS + LAIp_a +i])

    for i in range(LAIp_b + 1):
        LAI[EGS - LAIp_b + i - 1] = LAI_c +(LAI_d-LAI_c)*i/LAIp_b
    #print('LAI = ', LAI[EGS - LAIp_b +i])

    #LAId = LAI 
    LAI[EGS:]=LAI_d

    LAI = pd.Series(LAI)
    LAI = LAI.repeat(repeats = 24)
    LAI.index = range(8760)
    # ZATIAL!!!
    #SAI = LAI + 1
    return LAI

def SAI(LAI):
    """ Surface area index
    Simpson 2003 - skontroluj """
    temp = LAI + 1
    return temp   