# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:45:04 2019

@author: Hanka
"""


def cO3_nmolm3(cO3_ppb, P_kPa, T_C):
    """Conversion function for ozone concentration from ppb to nmol*m-3  
    CLRTAP (2017) chap 3, pg 25
    P_kPa denotes air pressure [kPa], T_C denotes air temperature [°C]"""
    cO3_nmolm3 = cO3_ppb * P_kPa * 1000 / (8.31447 * (T_C + 273.15))
    return cO3_nmolm3