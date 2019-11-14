"""
set the parameters for the emPY scripts
"""


##############################
#general settings


# set projection
projection={'proj': 'lcc',
 'lat_1': 46.24470138549805,
 'lat_2': 46.24470138549805,
 'lat_0': 46.24470138549805,
 'lon_0': 17.0,
 'x_0': 0,
 'y_0': 0,
 'a': 6370000.0,
 'b': 6370000.0,
 'units': 'm',
 'no_defs': True}

# set grid parameters
grid_params={'XCELL': 14131.86328125,
 'XORIG': -1335201.875,
 'YORIG': -685262.6875,
 'ni': 133,
 'nj': 169,
 'nlays':7 
     }


##############################
#settings for to_domain


# import inventory inputs
import inventory_input as inventory_input

# import dictionry from inventory input
dic_inv=inventory_input.d

#list of inventory inputs which you want to take in the domain
#uncoment if you want all  
list_inv=dic_inv.keys()
# or take just specific ones in list
#list_inv=['TNO_SK_2015_A']

#define outpu directory of the to domain
output_directory='/data/dusan/emPY/data/outputs-to_domain-skusanie'

#define all pollutant names which will be included in the model 
#the names need to be consistent with the dictionary in inventory_input file with keys in  def_emis  
emis_proc_names =['PM', 'SO2', 'NOX', 'CO', 'VOC', 'NMVOC', 'NMBVOC', 'CH4', 'NH3',
                  'HG', 'BZN', 'BAP', 'NO', 'NO2', 'PM10', 'PM10_EC', 'PM10_OC',
                  'PM_CCRS', 'PM_CPRM', 'PM2_5', 'PM2_5_EC', 'PM2_5_OC', 'PM2_5_SO4',
                  'PM2_5_NA', 'PM2_5_FCRS', 'PM2_5_FPRM', 'PM2_5_AS', 'PM2_5_CD',
                  'PM2_5_NI', 'PM2_5_PB', 'PM2_5_CR', 'PM2_5_CU', 'PM2_5_SE',
                  'PM2_5_ZN']

#set new pollutants if True, specify the path to the new_pollutants file  
new_pol_value=True #False
new_pol_file='/data/dusan/emPY/case_run/new_pollutants.csv'


#set True if you want to have regriding control check in output
check_regrid=True #False

#set mask out file for the area sources which can be creating using the mask_out tool in tools 
mask_area='/data/em/data/input/mask/SL_MP_BIG.npy'

#set shape file for masking out the point sources
mask_point='/data/em/data/input/mask/silesia_and_malopolska_common_boundary.shp'

#parameters for the stacks which do not contain parameters in the invetory input
#this default parameters will be use.
parameters = {}
parameters[1000000] = ('SO2', {31.69: {'height': 176.1, 'temperature': 368.4, 'velocity': 12.5, 'diameter': 6.8},
                                0.03: {'height': 125.9, 'temperature': 401.2, 'velocity': 10.4, 'diameter': 4.1},
                                   0: {'height':  33.3, 'temperature': 470.7, 'velocity':  8.2, 'diameter': 1.4}})
parameters[3000000] = ('SO2', {3.169: {'height': 111.2, 'temperature': 417.1, 'velocity': 10.7, 'diameter': 3.5},
                              0.3169: {'height':  53.3, 'temperature': 458.7, 'velocity': 11.1, 'diameter': 2.0},
                                   0: {'height':  36.2, 'temperature': 412.0, 'velocity':  9.5, 'diameter': 1.9}})
parameters[3400000] = parameters[3000000]
parameters[4000000] = ('CO',  {3.169: {'height':  39.0, 'temperature': 365.0, 'velocity': 10.4, 'diameter': 2.3},
                                0.03: {'height':  30.6, 'temperature': 396.4, 'velocity': 11.5, 'diameter': 1.5},
                                   0: {'height':  22.6, 'temperature': 435.8, 'velocity':  8.9, 'diameter': 1.3}})
parameters[5000000] = ('CH4', {0.3169: {'height':  27.7, 'temperature': 344.0, 'velocity':  1.7, 'diameter': 3.1},
                          0.000000317: {'height':  17.0, 'temperature': 301.3, 'velocity':  7.6, 'diameter': 1.5},
                                    0: {'height':  11.0, 'temperature': 307.7, 'velocity':  8.1, 'diameter': 0.9}})
parameters[6000000] = ('NMVOC',{0.3169: {'height':  16.1, 'temperature': 298.8, 'velocity':  9.1, 'diameter': 1.3},
                                 0.003: {'height':  11.0, 'temperature': 307.7, 'velocity':  8.1, 'diameter': 0.9},
                                     0: {'height':  13.6, 'temperature': 347.2, 'velocity':  7.0, 'diameter': 0.9}})
parameters[9000000] = ('PM10', {0.3169: {'height': 126.2, 'temperature': 398.1, 'velocity': 11.8, 'diameter': 2.2},
                                  0.03: {'height':  39.7, 'temperature': 402.3, 'velocity':  9.0, 'diameter': 1.6},
                                     0: {'height':  22.5, 'temperature': 391.2, 'velocity':  8.1, 'diameter': 1.2}})

parameters[10000000]=parameters[5000000]
parameters[8000000]=parameters[4000000]

##############################
#setting for speciate

#####
#set input directory
input_dir_speci='/data/dusan/EMPYS/data/outputs-to_grid-skusanie'
# set the output directory
output_dir_speci='/data/dusan/EMPYS/data/outputs-speciation-skusanie'
# set the aero spec file
specAERO_file='/data/em/manipulate_and_speciate/static_data/gspro_AE4+BAP.csv'

#set the spec GAS file
specGAS_file='/data/em/manipulate_and_speciate/static_data/gspro_CB05.csv'


#emission category file
em_cat_file='/data/dusan/EMPYS/speciate/emission_categories_sp.csv'

#list inventory if other than to domain
list_inv_spec=list_inv

#import os
#list for point sources
#list_point=os.listdir(input_dir_speci+'/point_sources')















