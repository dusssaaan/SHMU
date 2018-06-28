#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
changed grid dimensions in lines 43,44 in order to fit the RIO validation results

"""

__author__ = "Dusan Stefanik"


import netCDF4
import numpy as np
import pyproj

def sur(x,X,x00):
    """
    argument x - x(y) coordinate in m in LCC; X: XCELL (YCELL) of grid in m; x00 the x[0,0] (y[0,0]) coorinate of the domain  \n
    return xs - the j (i) indices of the domain
    """
    xs=(x-x00)/X
    return xs  

def indices(gridcro,lon_st,lat_st):
    """
    argument gridcro - GRIDCRO2D netcdf field, imported using Dataset; lon_st, lat_st - longitude and latitude of Topolniky station \n
    returns tuple (i,j,imin,jmin,imax,jmax, i_s, j_s) indices are described in the function \n
    the projection is set in function p
    """
    #projection
    p=pyproj.Proj("+proj=lcc +lat_1=46.24470138549805 +lat_2=46.24470138549805 +lat_0=46.24470138549805 +lon_0=17.0 +x_0=0.0 +y_0=0.0 +a=6370000.0 +b=6370000.0 +units=m +no_defs")

    grid=gridcro
    
    lon=np.array(grid.variables['LON'][0,0,1:102,1:180])
    lat=np.array(grid.variables['LAT'][0,0,1:102,1:180])

    X_CELL=grid.XCELL
    Y_CELL=grid.YCELL
    
    #conversion of grid  lon, lat to x,y  
    x_L, y_L = p(lon, lat, inverse=False)
    
    # station - x,y lambert coordinates
    x_s, y_s = p(lon_st, lat_st, inverse=False)
    
    # station - i,j coordinates
    i_s=sur(y_s,Y_CELL,y_L[0,0])
    j_s=sur(x_s,X_CELL,x_L[0,0])
      
        
    # station - closest i,j
    i=int(np.rint(i_s)) 
    j=int(np.rint(j_s)) 
    
    # station surounding i 
    imin=int(i_s)
    imax=imin+1
    
    # station surounding j 
    jmin=int(j_s)
    jmax=jmin+1
    
    
          
    return i,j,imin,jmin,imax,jmax, i_s, j_s



def bilinter(x,imin,jmin,imax,jmax,i_s,j_s):
    """
    argument x - two dimensional field; i_s,j_s -indices of desired place in which we want to provide interpolation; imin,jmin,imax,jmax: respective surounding indices of domain \n
    return bilinear interpolated value of the field x in place i_s,j_s according https://en.wikipedia.org/wiki/Bilinear_interpolation
    """
    bi_interpol=x[imin,jmin]*(imax-i_s)*(jmax-j_s)+x[imax,jmin]*(i_s-imin)*(jmax-j_s)+x[imin,jmax]*(imax-i_s)*(j_s-jmin)+x[imax,jmax]*(i_s-imin)*(j_s-jmin)
    return bi_interpol  







