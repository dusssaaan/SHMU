#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 08:28:31 2019

@author: p6001
"""
import numpy as np
import shapely
import time
import os


  
def line_to_domain(shape_file, output_dir, name, def_emis, inventory, projection, grid_params):

    if not os.path.exists(output_dir):
       os.makedirs(output_dir)
    
    XORIG=grid_params['XORIG']
    YORIG=grid_params['YORIG']
    XCELL=grid_params['XCELL']
    nj=grid_params['nj']
    ni=grid_params['ni']
    
    
    start_time = time.time()
    
    
    shape_file=shape_file.to_crs(projection)
      
      
    print('Processing cat: {}'.format(inventory))

    dic_out={}   
    
    for de in def_emis.keys():
        
        dic_out[de]=np.zeros([ni,nj])
             

            
    for index, em in shape_file.iterrows():
        
        pol2=shape_file['geometry'][index]
        
        a=pol2.bounds
    
        jmin=int((a[0]-XORIG)/(XCELL))
        jmax=int((a[2]-XORIG)/(XCELL))
        
        imin=int((a[1]-YORIG)/(XCELL))
        imax=int((a[3]-YORIG)/(XCELL))
               
        
                 
        if jmin < 0:
           jmin=0
        if imin < 0:
           imin=0
        if jmax > nj-1:
           jmax=nj-1 
        if imax > ni-1:
           imax=ni-1    
           
        if  not pol2.is_valid:
            pol2=pol2.buffer(0)
            print('Be carefull, polygon {} was bad definned, buffer(0) was used to repair it'.format(index))
        
                
        for i in range(imin,imax+1):
            for j in range(jmin,jmax+1):
                x=j*XCELL+XORIG
                y=i*XCELL+YORIG
                
                pol=shapely.geometry.box(x,y,x+XCELL,y+XCELL,ccw=True)
                
                                
                coef=pol2.intersection(pol).length/pol2.length
                 
                for de in def_emis:    
                    dic_out[de][i,j]=dic_out[de][i,j]+coef*em[de]
    
            
            
    for de in def_emis.keys():
        np.save('{0}/{1}-{2}-{3}'.format(output_dir,inventory,def_emis[de],name),  dic_out[de])  
            
    print("index ---{0}".format(index))
        
    print("Data are regrided in %s seconds ---" % (time.time() - start_time))    
    








def regridding_control(shape_file, output_dir, name, def_emis, inventory):
       
    
    for de in def_emis.keys():   
        
        sk=np.load('{0}/{1}-{2}-{3}.npy'.format(output_dir,inventory,def_emis[de],name)) 
               
            
        sk2=np.sum(shape_file[de])  
            
        a=np.sum(sk)
        b=np.sum(sk2)
        
        print('cat {0}, pollutant {1}, diference {2:.2f}'.format(inventory,def_emis[de], a-b))
        print('value in grid {0:.3f}'.format(a))
        print('value in source file {0:.3f}'.format(b))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    