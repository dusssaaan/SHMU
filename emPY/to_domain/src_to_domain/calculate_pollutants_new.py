#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:48:48 2019

@author: p6001
"""
import pandas as pd
import numpy as np


def calc_points(calculate_pol_file, emis_file_path):
     
    cal_pol=pd.read_csv(calculate_pol_file)
    data_frame=pd.read_csv(emis_file_path)
    
    print('##### calculate pollutants')
    
    def split(string):
        return string.split(',');
    
    cal_pol['expressions']=cal_pol[cal_pol.columns[1]].apply(split)
      
    for index, row in cal_pol.iterrows():
        cat=row[cal_pol.columns[0]]
        if cat in data_frame['SNAP_internal'].unique():
          
           for expression in row['expressions']:
               
               expression=expression.replace(' ','')
               exp_split=expression.split('=')
               pollutant_new=exp_split[0]
               
               if pollutant_new not in data_frame.columns:
                  
                  data_frame[pollutant_new]=np.nan
                                              
               mask=((data_frame[pollutant_new].isnull()) & (data_frame['SNAP_internal']==cat))   
               
               apply=data_frame[mask]
               
               if apply.shape[0] !=0 :
                   
                   print('Apply {0} on category {1} and  ISTACKS {2}'.format(expression,cat,list(apply['ISTACK'].unique())))
                   
                   not_apply=data_frame[~mask]
                   
                   try:
                       apply=apply.eval(expression)
                       data_frame=pd.concat([apply,not_apply],sort=False).sort_index()
                   except:
                        print('Warning: Expresion {0} on category {1} can not be applied !!!'.format(expression,cat))
                       
    
    data_frame=data_frame.replace(np.nan,0)    
    data_frame.to_csv('{0}'.format(emis_file_path),index=False)        
        