#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:55:40 2019

@author: p6001
"""
import time
import os
import numpy as np
import netCDF4
import datetime

coef=(10**6/(8760*3600))
def numpy_time_variation_matrix(input_dir,cmaq_sp,dic_time_matrix, dic_time_map,dim,nlays,ni,nj):
   
   
   
   start_time=time.time() 
    
   dic_species={}         
   for spec in cmaq_sp:
       dic_species[spec]=np.zeros([dim,nlays,ni,nj])
  
                                                                                                                                                                                                                                                                                                                                                                     
   for file in os.listdir(input_dir):
        f_split=file.split( "-" )
        
        if f_split[1][:-4] in dic_species.keys():
        
           if int(f_split[0]) in dic_time_map.keys():
            
              au=np.load('{0}/{1}'.format(input_dir,file))
            
                  
              au2=np.zeros([dim,au.shape[0],au.shape[1],au.shape[2]])
            
              for i in range(0,dim):
                  au2[i,:,:,:]=au[:,:,:]*dic_time_matrix[dic_time_map[int(f_split[0])]][i]
             
              dic_species[f_split[1][:-4]]+=au2
            
           else:
              print('{0}-{1} is not taking to time variation'.format(f_split[0],f_split[1][:-4])) 
    
   print('numpy arrays are done in {0:.1f} sec'.format(time.time() - start_time))  
   return dic_species;


#writing to netcdf ############################################################################
def gridded_to_netCDF_OLD(output_dir,out_file_name,dic_species,datum,projection,grid_params):
        
       
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
                    'CTIME':np.int32(63057),
                    'DATE_TIME':np.int32(2),
                    'EXEC_ID':"???????????????? ",
                    'FILEDESC':"Point source stack groups",
                    'FTYPE':np.int32(1),
                    'GDTYP':np.int32(2),
                    'HISTORY':"",
                    'IOAPI_VERSION':"Id",
                    'NC_STEP':np.int32(1),
                    'NLAYS':np.int32(grid_params['nlays']),
                    'NTHIK':np.int32(1),
                    'NVARS':np.int32(len(var_names.keys())),
                    'SDATE':np.int32(0),
                    'STIME':np.int32(0),
                    'TSTEP':np.int32(10000),
                    'UPNAM':"OPENEOUT        ",
                    'VAR-LIST':"".join('{0:16s}'.format(f) for f in var_names.keys()),
                    'VGLVLS':np.array([1., 0.993, 0.983, 0.97, 0.954, 0.934, 0.909, 0.88],dtype='float32'),
                    'VGTOP':np.float32(2000.),
                    'VGTYP':np.int32(7),
                    'WDATE':np.int32('{0}{1:03d}'.format(datetime.datetime.today().year,datetime.datetime.today().timetuple().tm_yday)),
                    'WTIME':np.int32(63057),
                    'NCOLS':np.int32(grid_params['nj']),
                    'NROWS':np.int32(grid_params['ni']),
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
             out.variables[name][:,:,:,:]=dic_species[name]*coef 
         




var_names = {'CO': ['moles/s', 'CO', 'Model species CO'],
                 'HONO': ['moles/s', 'HONO', 'Model species HONO'],
                 'NO': ['moles/s', 'NO', 'Model species NO'],
                 'NO2': ['moles/s', 'NO2', 'Model species NO2'],
                 'ACET': ['moles/s', 'ACET', 'Model species ACET'],
                 'ALD2': ['moles/s', 'ALD2', 'Model species ALD2'],
                 'ALD2_PRIMARY': ['moles/s', 'ALD2_PRIMARY', 'Model species ALD2_PRIMARY'],
                 'ALDX': ['moles/s', 'ALDX', 'Model species ALDX'],
                 'BENZ': ['moles/s', 'BENZ', 'Model species BENZ'],
                 'CH4': ['moles/s', 'CH4', 'Model species CH4'],
                 'ETH': ['moles/s', 'ETH', 'Model species ETH'],
                 'ETHA': ['moles/s', 'ETHA', 'Model species ETHA'],
                 'ETHY': ['moles/s', 'ETHY', 'Model species ETHY'],
                 'ETOH': ['moles/s', 'ETOH', 'Model species ETOH'],
                 'FORM': ['moles/s', 'FORM', 'Model species FORM'],
                 'FORM_PRIMARY': ['moles/s', 'FORM_PRIMARY', 'Model species FORM_PRIMARY'],
                 'IOLE': ['moles/s', 'IOLE', 'Model species IOLE'],
                 'ISOP': ['moles/s', 'ISOP', 'Model species ISOP'],
                 'KET': ['moles/s', 'KET', 'Model species KET'],
                 'MEOH': ['moles/s', 'MEOH', 'Model species MEOH'],
                 'NAPH': ['moles/s', 'NAPH', 'Model species NAPH'],
                 'NVOL': ['moles/s', 'NVOL', 'Model species NVOL'],
                 'OLE': ['moles/s', 'OLE', 'Model species OLE'],
                 'PAR': ['moles/s', 'PAR', 'Model species PAR'],
                 'PRPA': ['moles/s', 'PRPA', 'Model species PRPA'],
                 'SOAALK': ['moles/s', 'SOAALK', 'Model species SOAALK'],
                 'TERP': ['moles/s', 'TERP', 'Model species TERP'],
                 'TOL': ['moles/s', 'TOL', 'Model species TOL'],
                 'UNK': ['moles/s', 'UNK', 'Model species UNK'],
                 'UNR': ['moles/s', 'UNR', 'Model species UNR'],
                 'XYLMN': ['moles/s', 'XYLMN', 'Model species XYLMN'],
                 'NH3': ['moles/s', 'NH3', 'Model species NH3'],
                 'NH3_FERT': ['moles/s', 'NH3_FERT', 'Model species NH3_FERT'],
                 'SO2': ['moles/s', 'SO2', 'Model species SO2'],
                 'SULF': ['moles/s', 'SULF', 'Model species SULF'],
                 'PAL': ['g/s', 'PAL', 'Model species PAL'],
                 'PCA': ['g/s', 'PCA', 'Model species PCA'],
                 'PCL': ['g/s', 'PCL', 'Model species PCL'],
                 'PEC': ['g/s', 'PEC', 'Model species PEC'],
                 'PFE': ['g/s', 'PFE', 'Model species PFE'],
                 'PH2O': ['g/s', 'PH2O', 'Model species PH2O'],
                 'PK': ['g/s', 'PK', 'Model species PK'],
                 'PMG': ['g/s', 'PMG', 'Model species PMG'],
                 'PMN': ['g/s', 'PMN', 'Model species PMN'],
                 'PMOTHR': ['g/s', 'PMOTHR', 'Model species PMOTHR'],
                 'PNA': ['g/s', 'PNA', 'Model species PNA'],
                 'PNCOM': ['g/s', 'PNCOM', 'Model species PNCOM'],
                 'PNH4': ['g/s', 'PNH4', 'Model species PNH4'],
                 'PNO3': ['g/s', 'PNO3', 'Model species PNO3'],
                 'POC': ['g/s', 'POC', 'Model species POC'],
                 'PSI': ['g/s', 'PSI', 'Model species PSI'],
                 'PSO4': ['g/s', 'PSO4', 'Model species PSO4'],
                 'PTI': ['g/s', 'PTI', 'Model species PTI'],
                 'PMC': ['g/s', 'PMC', 'Model species PMC'],
                 'VOC_INV': ['g/s', 'VOC_INV', 'Model species VOC_INV']}








