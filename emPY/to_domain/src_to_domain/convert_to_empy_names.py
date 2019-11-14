"""
Created on Tue Oct  8 09:35:25 2019

@author: p6001
"""
import numpy as np
import pandas as pd

def new_pollutans(emis_file, new_pol_file_path):
     
    new_pol=pd.read_csv(new_pol_file_path)
        
    print('##### calculate pollutants')
    
    new_pol['expressions']=new_pol[new_pol.columns[1]].apply(lambda x: x.split(','))
      
    for index, row in new_pol.iterrows():
        cat=row[new_pol.columns[0]]
        if cat in emis_file['cat_internal'].unique():
          
           for expression in row['expressions']:
               
               expression=expression.replace(' ','')
               exp_split=expression.split('=')
               pollutant_new=exp_split[0]
               
               if pollutant_new not in emis_file.columns:
                  
                  emis_file[pollutant_new]=np.nan
                                              
               mask=((emis_file[pollutant_new].isnull()) & (emis_file['cat_internal']==cat))   
               
               apply=emis_file[mask]
               
               if apply.shape[0] !=0 :
                   
                   print('Apply {0} on category {1} '.format(expression,cat))
                   
                   not_apply=emis_file[~mask]
                   
                   try:
                       apply=apply.eval(expression)
                       emis_file=pd.concat([apply,not_apply],sort=False).sort_index()
                   except:
                        print('Warning: Expresion {0} on category {1} can not be applied !!!'.format(expression,cat))
                       
    
    return emis_file;

def csv_to_processor_names(emis_file, dic_inv,new_pol_value, new_pol_file_path):
   
    emis_file=emis_file.replace(np.nan,0)
    if 'filter' in dic_inv.keys():
        for filters in dic_inv['filter']:
        
            emis_file=emis_file.query(filters)
        
            print('filter {} was applied'.format(filters))
    

    
    emis_file=emis_file.rename(columns=dic_inv['def_emis'])
    
    convert_columns=['x', 'y', 'ID','height', 'diameter', 'temperature', 'velocity', 
                     'cat_internal','source_id']  #,'shape_id'
    
    for conversion in convert_columns:
        if conversion in dic_inv.keys():
           
           
           emis_file=emis_file.rename(columns={dic_inv[conversion]:conversion})
    
    emis_file=emis_file.rename(columns=dic_inv['def_emis'])
    
    pollutants=list(dic_inv['def_emis'].values())

    if 'emission_inventory' not in dic_inv.keys():
        emis_file['cat_internal']=dic_inv['one_cat']  
        #list_of_columns.append('cat_internal')
    else:
        emis_file=emis_file.replace({'cat_internal':dic_inv['emission_inventory']})
        emis_file=emis_file[emis_file['cat_internal'].isin(list(dic_inv['emission_inventory'].values()))]
        emis_file['cat_internal']=emis_file['cat_internal'].apply(int)
    
    print('')
    
    if dic_inv['units']=='kg/year':
       emis_file[pollutants]=emis_file[pollutants]/1000.0
       print('{} is in kg/year and its transformed to t/year'.format(pollutants))
    elif dic_inv['units']=='g/year':
       emis_file[pollutants]=emis_file[pollutants]/1000000.0
       print('{} is in g/year and its transformed to t/year'.format(pollutants))
    elif dic_inv['units']=='mg/year':
       emis_file[pollutants]=emis_file[pollutants]/1000000000.0
       print('{} is in mg/year and its transformed to t/year'.format(pollutants))
    elif dic_inv['units']=='kilot/year':
       emis_file[pollutants]=1000*emis_file[pollutants]
       print('{} is in kilot/year and its transformed to t/year'.format(pollutants))
    else:
       print('{0} is in {1} '.format(pollutants,dic_inv['units']))
    print('')      
    
    
    if new_pol_value==True:
       emis_file=new_pollutans(emis_file, new_pol_file_path)
             
    emis_file=emis_file.replace(np.nan,0)  
    
    #dokodovat ak bude uz stlpec s danym menom pritomny a preklad bude viazany 
    #vymazat ho aby tam nebol dva krat
    
    return emis_file;
 
    
def apply_stack_parameters(emis_file,parameters):

    emis_file['height']=0
    emis_file['temperature']=0
    emis_file['velocity']=0
    emis_file['diameter']=0
  
    for index, row in emis_file.iterrows():        
                
        cat=row['cat_internal']
                      
        param=parameters[cat]
        poll=param[0]
        
        keys=np.sort(list(param[1].keys()))
       
        for key in keys:
            if row[poll] >= key:
               height=param[1][key]['height'] 
               temperature=param[1][key]['temperature']-273.15 # pozor zatail je tam v params teplota v kelvinoch
               velocity=param[1][key]['velocity']
               diameter=param[1][key]['diameter'] 
         
               
        emis_file.loc[index,'height']=height 
        emis_file.loc[index,'temperature']=temperature
        emis_file.loc[index,'velocity']=velocity
        emis_file.loc[index,'diameter']=diameter     
              
           
   
    return emis_file;     


 





