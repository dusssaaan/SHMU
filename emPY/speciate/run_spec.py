#!/usr/bin/env /data/juraj/anaconda3/envs/geo/bin/python
# -*- coding: utf-8 -*-
"""

SPECIATION SCRIPT

Function:    
speciate all files from output_to_grid array 
according two gspro files

Libraries and modules needed:
libraries: pandas, numpy, time, geopandas, shapely, pyproj


Revision History:
    
29.01.2019 D. Stefanik: creating first version of script


"""
#####
#set path to case 
case_path='/data/dusan/EMPYS/case_run'


# imported libraries
import numpy as np
import pandas as pd
import os
import time
import sys
import importlib
import src_speciate.group_point_sources as gps

sys.path.append(case_path)
import config_file
importlib.reload(config_file)



grid_params=config_file.grid_params

projection=config_file.projection
#set input directory
input_dir=config_file.input_dir_speci
# set the output directory
output_dir=config_file.output_dir_speci
# set the aero spec file
specAERO=pd.read_csv(config_file.specAERO_file,comment='#',
                     names=['cat','old_name','spec_name','coef1','coef2','coef3'], header=0 )

#set the spec GAS file
specGAS=pd.read_csv(config_file.specGAS_file,comment='#',
                     names=['cat','old_name','spec_name','coef1','coef2','coef3'], header=0 )


#emission category file
em_cat_file=pd.read_csv(config_file.em_cat_file)

list_inv=config_file.list_inv_spec

list_point=config_file.list_point
list_point=[ 'POL_MP_point',
             'TNO_without_CZE_SK_SL_Malopolska_p',
             'REZZO_1_2',
             'SVK_snap_02_point',
             'POL_SL_point',
             'REZZO_4_ATEM_tunnel_all']

###########################################################################################################
start_time = time.time()


if os.path.exists(output_dir):
   
   print('deleting files in the {0} '.format(output_dir))
   
   os.system('rm -f {0}/*.npy'.format(output_dir))


#creating output directory
if not os.path.exists(output_dir):
   os.makedirs(output_dir)





###############################################################################
#Point sources
################################################################################
point_emissions=gps.stack_params_to_netCDF4(gps.group_point_sources(input_dir+'/point_sources',list_point),output_dir,grid_params,projection)


#merge two gspro file in one
spec=specAERO.append(specGAS)
#spec_names
spec_names=spec['spec_name'].unique()

for sp in spec_names:
    if sp not in point_emissions.columns:
       point_emissions[sp]=0 


for cat in spec['cat'].unique():
    print(cat)

    dic_speciate=dict(zip(spec[spec.cat==cat]['spec_name'], spec[spec.cat==cat]['old_name']))
    dic_koef=dict(zip(spec[spec.cat==cat]['spec_name'], spec[spec.cat==cat]['coef1']/spec[spec.cat==cat]['coef2']))
    profiles_speciate_as_cat=list(em_cat_file[em_cat_file.speciation_profile ==cat]['cat_id'].unique())
    
    
    if cat == 0:
    
        for sp in dic_speciate:
               
                print('Speciate {0} on category {1} with coeficient {2}*{3}'.format(sp,cat,dic_koef[sp],dic_speciate[sp]))
                
                point_emissions[sp]=point_emissions[dic_speciate[sp]]*dic_koef[sp]      
    
    else:
            
        mask=point_emissions['SNAP_internal'].isin(profiles_speciate_as_cat)
        
        if mask.any():
        
            apply=point_emissions[mask]
        
            for sp in dic_speciate:
               
                print('Speciate {0} on categories {1} as {2} with coeficient {3}*{4}'.format(sp,profiles_speciate_as_cat,cat,dic_koef[sp],dic_speciate[sp]))
                
                apply[sp]=apply[dic_speciate[sp]]*dic_koef[sp]             
                  
                not_apply=point_emissions[~mask] 
                
                point_emissions=pd.concat([apply,not_apply],sort=False).sort_index()

point_emissions=point_emissions[['SNAP_internal']+list(spec_names)]           
point_emissions=point_emissions.replace(np.nan,0)
  
point_emissions.to_csv(output_dir+'/point_sources/'+'speciate_points', index=False)    
##############################################################################################################################  



#########################################################################################################
# area emissions
#########################################################################################################

#define which pollutants will mapping to themselves
spec_from_all_categories=list(spec[spec.cat==0]['old_name'].unique())

#Making the dictionary spec_coef_them with keys category-pollutant_old_name-speciation_name
#and values are the speciation coeficients, for mapping to themselves 
spec_coef_them={}
for index, row in spec.iterrows():
    cat_em_au='{0}-{1}'.format(row['cat'],row['old_name'])
    if row['cat']==0:
       spec_coef_them['{0}-{1}'.format(cat_em_au,row['spec_name'])]=row['coef1']/row['coef2'] 

#making the list cat_em_sp with category-pollutant_old_name_string for speciation files
#and making the dictionary spec_coef with keys category-pollutant_old_name-speciation_name
#and values are the spciation coeficients 
cat_em_sp=[]
spec_coef={}
for index, row in spec.iterrows():
    cat_em_au='{0}-{1}'.format(row['cat'],row['old_name'])
    if row['cat']!=0:
       cat_em_sp.append(cat_em_au)
       spec_coef['{0}-{1}'.format(cat_em_au,row['spec_name'])]=row['coef1']/row['coef2']    
##########################################################################################

#search all files in output directory and write all category-pollutant_old_name_string if they are 
#defined in gspro files (in cat_em_sp and in spec_from_all_categories)        

cat_em_list=[]
for name in list_inv:
    for file in os.listdir('{0}/{1}'.format(input_dir,name)):
    #file_list.append(file)
        f_split=file.split( "-" )
        cat_em_au='{0}-{1}'.format(f_split[0],f_split[1])
        if f_split[1] in spec['old_name'].unique():
            cat_em_list.append(cat_em_au)
        #else:
        #   print('{0}-{1} is not taking into account'.format(f_split[0],f_split[1])) 

#produced file unique_cat_em with unique category-pollutant_old_name_string values from cat_em_list
df=pd.DataFrame()
df['cat_em']=cat_em_list
unique_cat_em=df.cat_em.unique()

############################################################################################


#making empty arrays with size nlays, ni, nj in dictionary with keys unique_cat_em
dic_pol={}
for c_e in unique_cat_em:
    #print(c_e)
    dic_pol[c_e]=np.zeros([grid_params['ni'],grid_params['nj']])
    

#merge all arrays to the dic_pol 
list_from_where=[]
for name in list_inv:
    for file in os.listdir('{0}/{1}'.format(input_dir,name)):
        #file_list.append(file)
        f_split=file.split( "-" )
        
        if '{0}-{1}'.format(f_split[0],f_split[1]) in unique_cat_em:
        
            auxilary_array=np.load('{0}/{1}/{2}'.format(input_dir,name,file)) 
                        
            dic_pol['{0}-{1}'.format(f_split[0],f_split[1])][:,:]+=auxilary_array[:,:] 
            
            list_from_where.append(file)
            

#speciation#########################
#making speciation for dic_pol

dic_mapping_themselves={}
dic_speciations={}
print('###################################making speciation####################################################')                
for cat_em in dic_pol.keys():
    c_split=cat_em.split('-')
    # mapping themselves
    if c_split[1] in spec_from_all_categories:
       for coef in spec_coef_them.keys():
           if coef.startswith('0-{}-'.format(c_split[1])): 
              k=spec_coef_them[coef] 
              coef_split=coef.split('-')
              #print(cat_em,c_split[0],coef_split[2],spec_coef_them[coef])
              np.save('{0}/{1}-{2}'.format(output_dir,c_split[0],coef_split[2]), k*dic_pol[cat_em])
        
              dic_mapping_themselves['{0}-{1}'.format(coef_split[2],cat_em)]=[s for s in list_from_where if s.startswith('{}-'.format(cat_em))]
    
    # not mapping themselves
    else:
       if  c_split[1] in specAERO['old_name'].unique():
        
          if int(c_split[0]) in dic_cat_spec_AERO.keys():
              
              
             spec_c=dic_cat_spec_AERO[int(c_split[0])]
              
             for coef in spec_coef.keys():
                 if coef.startswith('{0}-{1}-'.format(spec_c,c_split[1])):
                    k=spec_coef[coef] 
                    coef_split=coef.split('-')
                    np.save('{0}/{1}-{2}'.format(output_dir,c_split[0],coef_split[2]), k*dic_pol[cat_em]) 
                      
                    dic_speciations['{0}-{1}'.format(coef_split[2],cat_em)]=[s for s in list_from_where if s.startswith('{}-'.format(cat_em))] 
            
          else:
              print(cat_em,'not mapping')
            
       elif c_split[1] in specGAS['old_name'].unique():
              
          if  int(c_split[0]) in dic_cat_spec_GAS.keys():
           
             spec_c=dic_cat_spec_GAS[int(c_split[0])]
              
             for coef in spec_coef.keys():
                 if coef.startswith('{0}-{1}-'.format(spec_c,c_split[1])):
                    k=spec_coef[coef] 
                    coef_split=coef.split('-')
                    np.save('{0}/{1}-{2}'.format(output_dir,c_split[0],coef_split[2]), k*dic_pol[cat_em]) 
                               
                    dic_speciations['{0}-{1}'.format(coef_split[2],cat_em)]=[s for s in list_from_where if s.startswith('{}-'.format(cat_em))]       
                
          else:
                 print(cat_em,'not mapping')
                      
       else:
           print('#################danger pollutant not in gas or not in aero speciations ##################################')               
              


print('##################### Program run sucessfuly ########################################')
print("Data are speciated in %s seconds ---" % (time.time() - start_time))



############################Checking speciation and merging ###################################################################
print("Checking speciation and merging")


for poll in spec['spec_name'].unique():
    
    print('###########################################################')
    print(poll)
    print('###')
    print('mapping themselves:')      
    for keys in dic_mapping_themselves:
        if keys.startswith('{}-'.format(poll)):
           print(dic_mapping_themselves[keys])
    print('###')       
    print('speciating from files:')
    for keys in dic_speciations:
        if keys.startswith('{}-'.format(poll)):
           print(dic_speciations[keys])          
 


print("Speciation is checked in %s seconds ---" % (time.time() - start_time))




    
       