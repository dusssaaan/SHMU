#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
module containnig the functions which produces from the hourly values of concentrations the daily average and yearly average concentrations
"""
import numpy as np

#make daily avarage conc values
def daily(cctm_hourly):
    cctm_daily=np.empty((365,99,178))
    for i in range(0,365):
        z=i*24
        k=(i+1)*24
        cctm_daily[i,:,:]=np.average(cctm_hourly[z:k,:,:], axis=0)
    return cctm_daily

#make annual average coc values  
def annual(cctm_daily):
    cctm_ann=np.empty((99,178))
    cctm_ann[:,:]=np.average(cctm_daily[:,:,:], axis=0)
    return cctm_ann
  
def skusaj():
    print('de')  
    
    
    