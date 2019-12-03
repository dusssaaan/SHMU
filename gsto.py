# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:19:16 2019

@author: Anna
"""
import resistances2 as rs
import math
import pandas as pd
import numpy as np

#def fphen(day):
#    """ fphen is a phenology function. Method based on a fixed time interval. 
#    From CLRTAP (2017), chap 3, pg 19-20"""
#    if day >= rs.static_param("Astart_FD") and day < rs.static_param("Astart_FD") + rs.static_param("fphen_1FD"):
#        temp = (1-rs.static_param("fphen_a"))*((day -rs.static_param("Astart_FD")) / rs.static_param("fphen_1FD")) + rs.static_param("fphen_a")    
#    elif day >= (rs.static_param("Astart_FD") + rs.static_param("fphen_1FD")) and day <= rs.static_param("Aend_FD") + rs.static_param("fphen_4FD"):
#        temp = 1
#    elif day > rs.static_param("Aend_FD") + rs.static_param("fphen_4FD") and day <= rs.static_param("Aend_FD"):
#        temp = (1-rs.static_param("fphen_e"))*((rs.static_param("Aend_FD") - day) / rs.static_param("fphen_4FD")) + rs.static_param("fphen_e")
#    else:
#        temp = 0
#    return temp

def fphen(day):
    """ fphen is a phenology function. Method based on a fixed time interval. 
    From CLRTAP (2017), chap 3, pg 19-20"""
    if day >= rs.static_param("Astart_FD") and day < rs.static_param("Astart_FD") + rs.static_param("fphen_1FD"):
        temp = (1-rs.static_param("fphen_a"))*((day -rs.static_param("Astart_FD")) / rs.static_param("fphen_1FD")) + rs.static_param("fphen_a")    
    elif day >= (rs.static_param("Astart_FD") + rs.static_param("fphen_1FD")) and day <= rs.static_param("Aend_FD") + rs.static_param("fphen_4FD"):
        temp = 1
    elif day > rs.static_param("Aend_FD") + rs.static_param("fphen_4FD") and day <= rs.static_param("Aend_FD"):
        temp = (1-rs.static_param("fphen_e"))*((rs.static_param("Aend_FD") - day) / rs.static_param("fphen_4FD")) + rs.static_param("fphen_e")
    else:
        temp = 0
    return temp

def fphen_year(n_days = 365):
    year = pd.Series(np.arange(1,n_days+1))
    fphen_y = year.apply(fphen)
    fphen_y = fphen_y.repeat(repeats = 24)
    fphen_y.index = range(8760)
    return fphen_y


def fleaf_light(R):
    """ fleaf_light is a function which describes leaf stomata respond to light
      From CLRTAP (2017), chap 3, pg 20"""    
    # PPFD = R/0.486263
    return(1 - math.e**(-rs.static_param("light_a") * (R/0.486263)))

    
def SVP(T_C): 
    """SVP saturated water pressure. Different approaches. 
    temp = 0.611 kPa * math.e ** (17.502 * T[°C]/(T[°C] + 240.97[°C])) # From Campbell and Norman 2000 (CLRTAP 2017)
    temp = 0.61078 *math.e**(17.27*T[°C]/(T[°C]+237.3))) # Tetens formula in [Pa] https://en.wikipedia.org/wiki/Vapour_pressure_of_water
    temp = 610.7*(10**(7.5*T/(T+237.3))) # [Pa]
    T_C denotes air temperature [°C]""" 
    temp = 0.611 * math.e ** (17.502 * T_C/(T_C + 240.97))
    return temp 

def VPD(RHper, SVP):
    """Vapour pressure deficit. 
    CLRTAP 2017 [kPa]. 
    """
    return(100 - RHper)/100*SVP/1000 # [kPa] 

def fVPD(VPD):
    """fVPD Function of leaf stomata respond to air humidity.
    CLRTAP (2017) chap 3, pg 22"""
    temp = ((1 - rs.static_param("fmin"))*(rs.static_param("VPDmin") - VPD)/(rs.static_param("VPDmin") - rs.static_param("VPDmax")) + rs.static_param("fmin"))
    temp = rs.apply_max(temp)
    temp = rs.apply_min(temp)
    return temp  

def ftemp(T_C):
    """ ftemp Function of leaf stomata respond to air temperature [°C]
    CLRTAP (2017) chap 3, pg 21
    T_C denotes air temperature [°C]"""
    bt = (rs.static_param("Tmax") - rs.static_param("Topt")) / (rs.static_param("Topt") - rs.static_param("Tmin"))
    if (T_C > rs.static_param("Tmin")) and (T_C < rs.static_param("Tmax")):
        temp = ((T_C - rs.static_param("Tmin")) / (rs.static_param("Topt") - rs.static_param("Tmin")))*((rs.static_param("Tmax")- T_C) / (rs.static_param("Tmax") - rs.static_param("Topt")))**bt
        temp = rs.apply_max(temp)
        return temp
    else:
        return rs.static_param("fmin")
 

def gstol(fphen, fleaf_light, fVPD, ftemp):
    """Based od Jarvis 1976 - The interpretation of the variations in leaf water potential and stomatal conductance found in canopies in the field.
    and improved by Emberson 2000, Simpson et al. 2012, CLRTAP 2017 (chap 3, pg 17)
    gstol and gmax [mmol O3 m-2 PLA s-1]"""
    temp = rs.static_param("gmax") * fphen * fleaf_light * (ftemp * fVPD).apply(rs.apply_max)#  max(fmin, ftemp * fVDP)
    return temp
