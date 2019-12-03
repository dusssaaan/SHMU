# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def Fstl(cO3_nmolm3, Rsur, Rb, gstol):
    ''' Hourly stomatal flux of ozone to vegetation[$nmol/ m^2 / s$]. 
    CLRTAP 2017 chap 3, pg. 25.'''
    aa = cO3_nmolm3 * (Rsur / (Rsur + Rb)) * gstol /41000
    return aa


 