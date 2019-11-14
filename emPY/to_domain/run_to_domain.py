#!/usr/bin/env /data/juraj/anaconda3/envs/geo/bin/python
"""
Function:    
regridding the year emission inventory files to the grid, 
files should be defined in inventory_input file acording rules

Libraries and modules needed:
libraries: pandas, numpy, time, geopandas, shapely, pyproj, importlib
modules:
src.area_to_domain - read shape files and csv with area sources and gridding them
src.line_to_domain - read shape files for line sources gridding them
src.point_to_domain_zero - read shape files and csv with point sources and gridding them, 
                                just in the 
src.calculate_pollutants - calculate pollutants defined in file calc_poll
    

Revision History:
    
28.01.2019 D.Stefanik: creating first version of script
31.10.2019 D.Stefanik: major revision of the sc
"""
#####
#set path to case 
case_path='/data/dusan/emPY/case_run'

#####Import libraries and modules
#import python libraries
import pandas as pd
import geopandas as gpd
import shapely
import pyproj
import numpy as np
import time 
import os
import sys
import importlib

#import config file
sys.path.append(case_path)
import config_file
importlib.reload(config_file)
#import libraries
import src_to_domain.area_to_domain as area_to_domain 
import src_to_domain.line_to_domain as line_to_domain 
import src_to_domain.point_to_domain_zero as point_to_domain_zero
import src_to_domain.point_to_domain as point_to_domain
import src_to_domain.convert_to_empy_names as convert_to_empy_names

#### read parameters from config file
# set projection
projection=config_file.projection


# set grid params
grid_params=config_file.grid_params

#read internal processor names
emis_proc_names=config_file.emis_proc_names

# read inventory input
dic_inv=config_file.dic_inv

# read case names wnich needed
list_inv=config_file.list_inv
list_inv=['REZZO_4_ATEM_road_all', 'REZZO_1_2', 'REZZO_4_ATEM_tunnel_all', 'PRG_apt_anti_ice', 'PRG_apt_deicing', 'PRG_apt_LTO_land', 'PRG_apt_engine_test', 'PRG_apt_fueling', 'PRG_apt_ops_tech_b', 'PRG_apt_ops_tech_d', 'PRG_apt_L_air', 'PRG_apt_TO_air', 'TNO_without_CZE_SK_SL_Malopolska', 'TNO_without_CZE_SK_SL_Malopolska_p', 'BaP_Europe_2015_A', 'BaP_Europe_2015_P', 'SVK_resHeat_15_85', 'SVK_snap_02_point', 'POL_MP_roadTransp_LR10_bochenski', 'POL_MP_roadTransp_LR10_brzeski', 'POL_MP_roadTransp_LR10_dabrowski', 'POL_MP_roadTransp_LR10_gorlicki', 'POL_MP_roadTransp_LR10_chrzanowski', 'POL_MP_roadTransp_LR10_Krakow_city', 'POL_MP_roadTransp_LR10_krakowski', 'POL_MP_roadTransp_LR10_limanowski', 'POL_MP_roadTransp_LR10_miechowski', 'POL_MP_roadTransp_LR10_myslenicki', 'POL_MP_roadTransp_LR10_nowosadecki', 'POL_MP_roadTransp_LR10_nowy_sacz_city', 'POL_MP_roadTransp_LR10_olkuski', 'POL_MP_roadTransp_LR10_oswiecimski', 'POL_MP_roadTransp_LR10_proszowicki', 'POL_MP_roadTransp_LR10_suski', 'POL_MP_roadTransp_LR10_tarnowski', 'POL_MP_roadTransp_LR10_tatrzanski', 'POL_MP_roadTransp_LR10_Tranow_city', 'POL_MP_roadTransp_LR10_wadowicki', 'POL_MP_roadTransp_LR10_wielicki', 'POL_MP_roadTransp_NR10', 'POL_MP_roadTransp_VR10', 'POL_MP_roadTransp_LR25', 'POL_MP_roadTransp_NR25', 'POL_MP_roadTransp_VR25', 'POL_SL_roadTransp_kraj', 'POL_SL_roadTransp_woj', 'POL_SL_roadTransp_PiG', 'POL_MP_point', 'POL_SL_point', 'POL_MP_resHeat_15_85_10', 'POL_MP_resHeat_15_85_25', 'POL_SL_resHeat_15_85', 'POL_MP_unorg_10', 'POL_MP_unorg_25', 'POL_SL_unorg', 'POL_MP_agri_machines_wadowicki', 'POL_MP_agri_machines_bochenski', 'POL_MP_agri_machines_brzeski', 'POL_MP_agri_machines_chrzanowski', 'POL_MP_agri_machines_dabrowski', 'POL_MP_agri_machines_gorlicki', 'POL_MP_agri_machines_krakowski', 'POL_MP_agri_machines_limanowski', 'POL_MP_agri_machines_miechowski', 'POL_MP_agri_machines_myslenicki', 'POL_MP_agri_machines_nowosadecki', 'POL_MP_agri_machines_nowotarski', 'POL_MP_agri_machines_olkuski', 'POL_MP_agri_machines_oswiecimski', 'POL_MP_agri_machines_proszowicki', 'POL_MP_agri_machines_suski', 'POL_MP_agri_machines_tarnowski', 'POL_MP_agri_machines_tatrzanski', 'POL_MP_agri_machines_wielicki', 'POL_MP_agri_machines_towns', 'POL_MP_agri_cf_towns', 'POL_SL_agri_machines', 'POL_SL_agri_cf', 'POL_MP_agri_cf_bochenski', 'POL_MP_agri_cf_brzeski', 'POL_MP_agri_cf_chrzanowski', 'POL_MP_agri_cf_dabrowski', 'POL_MP_agri_cf_gorlicki', 'POL_MP_agri_cf_krakowski', 'POL_MP_agri_cf_limanowski', 'POL_MP_agri_cf_miechowski', 'POL_MP_agri_cf_myslenicki', 'POL_MP_agri_cf_nowosadecki', 'POL_MP_agri_cf_nowotarski', 'POL_MP_agri_cf_olkuski', 'POL_MP_agri_cf_oswiecimski', 'POL_MP_agri_cf_proszowicki', 'POL_MP_agri_cf_suski', 'POL_MP_agri_cf_tarnowski', 'POL_MP_agri_cf_tatrzanski', 'POL_MP_agri_cf_wadowicki', 'POL_MP_agri_cf_wielicki', 'POL_SL_agri_livestock', 'POL_MP_agri_livestock_urban', 'POL_MP_agri_livestock_zone']
#define output directory
output_directory=config_file.output_directory

#set new pollutants
new_pol_value=config_file.new_pol_value
if new_pol_value == True:
   new_pol_file_path=config_file.new_pol_file
else:
   new_pol_file_path='no_file'

#set True if you want to have regriding control check in output
check_regrid=config_file.check_regrid

#set mask out file for the area sources
mask_area=config_file.mask_area

#set shape file for masking out the point sources
mask_point=config_file.mask_point



###############################################################################
print('The regriding will be do for {}'.format(list(list_inv)), flush=True)

start_time_of_whole_program = time.time()



#testing if input files in dictionaries exist

for name in list_inv:
     
    au=dic_inv[name]
    
    if 'input_file' in au.keys():
        if not os.path.isfile(au['input_file']):
           print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
           print('Input File {} does not exist'.format(au['input_file'])) 
        
    if 'shape_file' in au.keys():    
        if not os.path.isfile(au['shape_file']):
          print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
          print('Input File {} does not exist'.format(au['shape_file']))    
 

        
for name in list_inv:    
      
    print('####################################################################')
    print('Regrriding the {} inventory'.format(name))
   
    output_dir='{0}/{1}'.format(output_directory,name)
    
    if os.path.exists(output_dir):
       
       print('deleting files in the {0}/{1} inventory'.format(output_directory,name))
       
       os.system('rm -f {0}/{1}/*.npy'.format(output_directory,name))
       

    au=dic_inv[name]
    def_emis=au['def_emis']
    
    #area sources  
    if au['source_type'] == 'A' or au['source_type'] == 'L':
        
        if au['source_type'] == 'L':
           au['type']='shape'            
    
        if au['type']== 'csv+shape':
           
           emis_file=pd.read_csv(au['input_file'],sep=au['sep'], encoding=au['encoding'])
           emis_file=convert_to_empy_names.csv_to_processor_names(emis_file,au,new_pol_value, new_pol_file_path)
           emis_file['IJ']=emis_file['source_id']
           
           shape_file=gpd.read_file(au['shape_file'], encoding='utf-8')
           shape_file['IJ']=shape_file[au['shape_id']]
        
        elif au['type']== 'csv':
                       
            
           emis_file=pd.read_csv(au['input_file'],sep=au['sep'], encoding=au['encoding'])
                      
           min_x=np.min(emis_file[au['x']])
           min_y=np.min(emis_file[au['y']])
                      
           emis_file=convert_to_empy_names.csv_to_processor_names(emis_file,au,new_pol_value, new_pol_file_path)
           emis_file['IJ']=10000+(emis_file['x']-min_x)/au['grid_dx']*10000+(emis_file['y']-min_y)/au['grid_dy']           
           emis_file['IJ']=emis_file['IJ'].apply(int)   
                     
           shape_file=gpd.GeoDataFrame()
           shape_file['IJ']=emis_file['IJ']
           shape_file['geometry'] = list(zip(emis_file['x']-au['grid_dx']/2.0, emis_file['y']-au['grid_dy']/2.0,emis_file['x']+au['grid_dx']/2.0,emis_file['y']+au['grid_dy']/2.0))
           shape_file=shape_file.drop_duplicates()      
           def apply_args(argument):
               return shapely.geometry.box(*argument,ccw=True)    
           shape_file['geometry'] = shape_file['geometry'].apply(apply_args)
           shape_file.crs = "+init=epsg:{0}".format(au['EPSG'])

        elif au['type']== 'shape':
           
           shape_file=gpd.read_file(au['shape_file'], encoding='utf-8')
           shape_file['IJ']=shape_file.index
           
           emis_file=shape_file                 
           emis_file=convert_to_empy_names.csv_to_processor_names(emis_file,au,new_pol_value, new_pol_file_path)          
        
        if 'mask_out' in au.keys():
            mask_out=mask_area      
        else:
           mask_out=False 
      
        
        area_to_domain.area_to_grid(emis_file, shape_file, output_dir, name, def_emis, projection, grid_params,au['source_type'],mask_out)
        
        if check_regrid==True:
           area_to_domain.regridding_control(emis_file, shape_file, output_dir, name, def_emis, projection, grid_params)

########################################################################################################         
#point sources
#          
########################################################################################################          
    if au['source_type'] == 'P':
    
        if au['type']== 'csv':
           emis_file=pd.read_csv(au['input_file'],sep=au['sep'], encoding=au['encoding'])
           
           inProj = pyproj.Proj(init='epsg:{0}'.format(au['EPSG']))
              
        if au['type']== 'shape':
            
           emis_file=gpd.read_file(au['shape_file'], encoding='utf-8') 
            
           inProj = pyproj.Proj(emis_file.crs)
           emis_file['x']=emis_file['geometry'].x
           emis_file['y']=emis_file['geometry'].y
               
        emis_file=convert_to_empy_names.csv_to_processor_names(emis_file,au,new_pol_value, new_pol_file_path) 
        
        if 'mask_out' in au.keys():
            mask_out=mask_point
        else:
            mask_out=False 
        
        if au['def_heights']== False:
           
           emis_file=convert_to_empy_names.apply_stack_parameters(emis_file,config_file.parameters)  
          
        if au['def_heights']=='zero':
           point_to_domain_zero.point_to_domain(emis_file,output_dir, name, def_emis, projection, inProj, grid_params, mask_out)
        
           if check_regrid==True:
                             
              point_to_domain_zero.regridding_control(emis_file, output_dir, name, def_emis, projection, inProj, grid_params)
        
        if au['def_heights'] != 'zero':
           nove=point_to_domain.point_to_domain(emis_file,output_dir, name, def_emis, projection, inProj, grid_params, emis_proc_names, mask_out)

                                          
print('###############################################################################')
print('Program run sucessfully!')        
print('All data are in domain {0:.3f}'.format(time.time() - start_time_of_whole_program))
















