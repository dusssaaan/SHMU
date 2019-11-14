#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:51:06 2019

@author: p6001
"""
import pandas as pd
import numpy as np
import time
import copy
import os
import datetime
import netCDF4
import pyproj


coef=(10**6/(8760*3600))

def point_data_frame(point_path,cmaq_sp):
    
    points=pd.read_csv(point_path)
     
    for i in cmaq_sp:
        if i not in points.columns:
            points[i]=0 
       
    return points;


def time_profiles(dic_time_map,em_cat_file,points):
    
    print('################################################')
    print('point time variation chcek')
    
    snap_internal=set(list(points['SNAP_internal'].unique()))
    
    list_time_categories_used=[]
    profiles_used_in_time=[]
    for cat in list(set([x for x in dic_time_map.values()])):
           
        profile_time_as_cat=list(em_cat_file[em_cat_file.time_profile ==cat]['cat_id'].unique())
            
        if set(profile_time_as_cat) & snap_internal:
                      
            
           list_time_categories_used.append(cat)
           profiles_used_in_time+=profile_time_as_cat
           
           print('The categories {0} will be time variate as {1}'.format(profile_time_as_cat,cat))
           
    for i in snap_internal:
        if i not in profiles_used_in_time:
            
           print('WARNING {} is not time varried !!!!!!!!!'.format(i)) 
    print('################################################')
    
    return list_time_categories_used;        

def arrays(list_time_categories_used,em_cat_file,points,dim,dic_time_matrix,cmaq_sp):

    start_time = time.time()
    dic_time={}
    for i in range(0,dim):
        dic_time[i]=copy.deepcopy(points)
    
        for cat in list_time_categories_used:
            
            profile_time_as_cat=list(em_cat_file[em_cat_file.time_profile ==cat]['cat_id'].unique())
                                  
            dic_time[i].loc[(dic_time[i].SNAP_internal.isin(profile_time_as_cat)), cmaq_sp]*= dic_time_matrix[cat][i]
    
    dic_final={}

    for sp in cmaq_sp:
        dic_final[sp]=np.zeros([25,1,points.shape[0],1])
        for i in range(0,25):
            dic_final[sp][i,0,:,0]=dic_time[i][sp]
        
    
    print('Program run succesfully:-) in {0:.1f} sec'.format(time.time() - start_time)) 
    
    return dic_final;    

def point_to_netCDF(output_dir,out_file_name,dic_species,datum,projection,grid_params):
        
       
    if not os.path.exists(output_dir):
       os.makedirs(output_dir)
    
    var_names = {'PAR': ['moles/s', 'PAR', 'Model species PAR'],
                 'PNO3': ['g/s', 'PNO3', 'Model species PNO3'],
                 'PMFINE': ['g/s', 'PMFINE', 'Model species PMFINE'],
                 'BAP': ['g/s', 'BAP', 'Model species BAP'],
                 'IOLE': ['moles/s', 'IOLE', 'Model species IOLE'],
                 'PSO4': ['g/s', 'PSO4', 'Model species PSO4'],
                 'PEC': ['g/s', 'PEC', 'Model species PEC'],
                 'CO': ['moles/s', 'CO', 'Model species CO'],
                 'POC': ['g/s', 'POC', 'Model species POC'],
                 'SO2': ['moles/s', 'SO2', 'Model species SO2'],
                 'OLE': ['moles/s', 'OLE', 'Model species OLE'],
                 'ISOP': ['moles/s', 'ISOP', 'Model species ISOP'],
                 'TERP': ['moles/s', 'TERP', 'Model species TERP'],
                 'NO2': ['moles/s', 'NO2', 'Model species NO2'],
                 'ALDX': ['moles/s', 'ALDX', 'Model species ALDX'],
                 'CH4': ['moles/s', 'CH4', 'Model species CH4'],
                 'NH3': ['moles/s', 'NH3', 'Model species NH3'],
                 'ETOH': ['moles/s', 'ETOH', 'Model species ETOH'],
                 'ETHA': ['moles/s', 'ETHA', 'Model species ETHA'],
                 'FORM': ['moles/s', 'FORM', 'Model species FORM'],
                 'TOL': ['moles/s', 'TOL', 'Model species TOL'],
                 'PMC': ['g/s', 'PMC', 'Model species PMC'],
                 'ETH': ['moles/s', 'ETH', 'Model species ETH'],
                 'ALD2': ['moles/s', 'ALD2', 'Model species ALD2'],
                 'NO': ['moles/s', 'NO', 'Model species NO'],
                 'MEOH': ['moles/s', 'MEOH', 'Model species MEOH'],
                 'XYL': ['moles/s', 'XYL', 'Model species XYL'],
                 'BENZENE': ['moles/s', 'BENZENE', 'Model species BENZENE'],
                 'NR': ['moles/s', 'NR', 'Model species NR']} 
    
    
    
    global_params={ 'CDATE':np.int32('{0}{1:03d}'.format(datetime.datetime.today().year,datetime.datetime.today().timetuple().tm_yday)),
                    'P_ALP':projection['lat_1'],
                    'P_BET':projection['lat_2'],
                    'P_GAM':projection['lon_0'],
                    'XCENT':projection['lon_0'],
                    'YCENT':projection['lat_0'],
                    'PROJ4':pyproj.Proj(projection).definition_string(),
                    'CTIME':np.int32(63057),
                    'DATE_TIME':np.int32(2),
                    'EXEC_ID':"???????????????? ",
                    'FILEDESC':"Point source stack groups",
                    'FTYPE':np.int32(1),
                    'GDTYP':np.int32(2),
                    'HISTORY':"",
                    'IOAPI_VERSION':"Id",
                    'NC_STEP':np.int32(1),
                    'NLAYS':np.int32(1),
                    'NTHIK':np.int32(1),
                    'NVARS':np.int32(len(var_names.keys())),
                    'SDATE':np.int32(0),
                    'STIME':np.int32(0),
                    'TSTEP':np.int32(10000),
                    'UPNAM':"OPENEOUT        ",
                    'VAR-LIST':"".join('{0:16s}'.format(f) for f in var_names.keys()),
                    'VGLVLS':np.array([0., 0.],dtype='float32'),
                    'VGTOP':np.float32( -9.e+36),
                    'VGTYP':np.int32(-9999),
                    'WDATE':np.int32('{0}{1:03d}'.format(datetime.datetime.today().year,datetime.datetime.today().timetuple().tm_yday)),
                    'WTIME':np.int32(63057),
                    'NCOLS':np.int32(1),
                    'NROWS':np.int32(dic_species[list(dic_species.keys())[0]].shape[2]),
                    'XORIG':grid_params['XORIG'],
                    'YORIG':grid_params['YORIG'],
                    'XCELL':grid_params['XCELL'],
                    'YCELL':grid_params['XCELL'],
                    'GDNAM':"Stacks_nov_grid "}
   
    
    with netCDF4.Dataset('{0}/{1}-{2}.nc'.format(output_dir,out_file_name,datum.isoformat()[:-9]),mode='w') as out:
    
         # create globals
         for global_par in global_params:
                         
            out.setncattr(global_par, global_params[global_par])

         # create dimensions
        
         out.createDimension('TSTEP', None)
         out.createDimension('DATE-TIME', size=global_params['DATE_TIME'])
         out.createDimension('LAY', size=global_params['NLAYS'])
         out.createDimension('VAR', size=global_params['NVARS'])
         out.createDimension('COL', size=global_params['NCOLS'])
         out.createDimension('ROW', size=global_params['NROWS'])
         
         # create TFLAGS
         out.createVariable('TFLAG', np.int32, ('TSTEP', 'VAR', 'DATE-TIME'),fill_value=None)
         out.variables['TFLAG'].setncatts({'units': "<YYYYDDD,HHMMSS>", 'long_name': "FLAG", 'var_desc': "Timestep-valid flags:  (1) YYYYDDD or (2) HHMMSS"})     
         
         
         tflag=np.zeros([25,global_params['NVARS']],dtype=int)
         for i in range(1,24):
             tflag[i,:]=int(i*10000)
         
         out.variables['TFLAG'][:,:,1]=tflag   
         out.variables['TFLAG'][:24,:,0]=int('{0}{1:03d}'.format(datum.year,datum.timetuple().tm_yday))
         datum_next=datum+datetime.timedelta(days=1)
         out.variables['TFLAG'][24,:,0]=int('{0}{1:03d}'.format(datum_next.year,datum_next.timetuple().tm_yday))
                  
         # create variables
         for name in var_names:
             
             out.createVariable(name, np.float32, ('TSTEP', 'LAY', 'ROW', 'COL'),fill_value=None)
             out.variables[name].setncatts({'units': var_names[name][0], 'long_name': var_names[name][1], 'var_desc': var_names[name][2]})     
             print(dic_species[name].shape)
             print(out.variables[name].shape)
             out.variables[name][:,:,:,:]=dic_species[name]*coef 









