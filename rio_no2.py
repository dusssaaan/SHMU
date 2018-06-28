#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script that compare CMAQ model with RIO results

@author: p6001
"""

import h5py
import numpy as np
import geopandas as gpd
import pandas as pd
import netCDF4
from pyproj import Proj, transform
import matplotlib.pyplot as plt
import csv
import bi_in2

import importlib
importlib.reload(bi_in2)

element='no2'
subor=8
aa=1.9125

element_netcdf=element
if element == 'pm10' or element == 'pm25':
     element_netcdf='pm' 



###################################################################################################################
#read inputs files
#
#
###################################################################################################################

#rio hdf5 file
file = h5py.File('/media/sf_Share/LifeIP_results_RIO/LifeIP_results_RIO/NO2/2015_RIO_output_daily_average/rio_no2_da_pop_47x47_20150101-20151231.h5','r')
#rio grid with X2, Y2 coordinates
grid=gpd.read_file('/media/sf_Share/LifeIP_results_RIO/grid/grid/CAMx_d02.shp')
#cmaq grid
grid_CMAQ=netCDF4.Dataset('/data/mala/GRIDCRO2D_01012015.nc')
#cmaq data
model_CMAQ=netCDF4.Dataset('/media/sf_Share/TERKA/LIFEIP_Small_{0}_2015'.format(element_netcdf.upper()))



######################################################################################################
#list all data from RIO HDF5 format and save all data in dictionary data
#Print all directories and atributes from the hdf5 
#
#
######################################################################################################

#list all hdf
a=list(file.keys())


priecinky={}
for i in a:
    b=list(file[i])
    priecinky[i]=b
    
    
data={}   
keys=priecinky.keys()
for i in keys:
    for j in priecinky[i]:
        atr=file['{0}/{1}'.format(i,j)].attrs.keys()
        data['{0}/{1}'.format(i,j)]=file['{0}/{1}'.format(i,j)]
        print(i,j,list(atr))
        for k in list(atr):
            print(file['{0}/{1}'.format(i,j)].attrs[k])
            
###########################################################################################################################
#
#prepare CMAQ and RIO daily and annual average field 
#
#
###########################################################################################################################

cmaq_hourly=np.array(aa*model_CMAQ.variables[element.upper()][:,0,1:102,1:180])

# make daily average cmaq values
cmaq_daily=np.empty((365,101,179))
for i in range(0,365):
    z=i*24
    k=(i+1)*24
    cmaq_daily[i,:,:]=np.average(cmaq_hourly[z:k,:,:], axis=0)


#make annual average cmaq values
cmaq_ann=np.empty((101,179))
cmaq_ann[:,:]=np.average(cmaq_daily[:,:,:], axis=0)


#rio value
rio_daily=np.array(data['grid/value'][:])
rio_daily=np.reshape(rio_daily,(101,179,365))

#rio annual average
rio_ann=np.empty((101,179))
rio_ann=np.average(rio_daily[:,:,:], axis=2)

annual_dif_per=(cmaq_ann-rio_ann)/rio_ann*100

annual_dif=(cmaq_ann-rio_ann)

#############################################################################################################################
#
#
# prepare file for R script for annual and daily statistics for the cells
#
#
##############################################################################################################################

#hourly stat 

rio_ann_fl=rio_ann.flatten()
cmaq_ann_fl=cmaq_ann.flatten()

with open('/data/rio/{0}/{0}_ann_cell.csv'.format(element), 'wt') as an, open('/data/rio/{0}/{0}_day_cell.csv'.format(element), 'wt') as da:
     writeran = csv.writer(an)
     writeran.writerow( ('cell','rio','cmaq')) 

     for j in range(0,rio_ann_fl.shape[0]):
         writeran.writerow((j,rio_ann_fl[j],cmaq_ann_fl[j]))
     
#daily stat      
      
     writerda = csv.writer(da)
     writerda.writerow( ('cell','date','rio','cmaq'))  
      
      
     for j in range(0,365):
         
         rio_da_fl=rio_daily[:,:,j].flatten()
         cmaq_da_fl=cmaq_daily[j,:,:].flatten()
                        
         for k in range(0,rio_da_fl.shape[0]):
             writerda.writerow((k,'{0}-{1:02d}-{2:02d}'.format(data['time/year'][j],data['time/month'][j],data['time/day'][j]),rio_da_fl[k],cmaq_ann_fl[k]))
         
         print(j) 
      
#############################################################################################################################
#
#
# make time series for the individual stations 
#
#
##############################################################################################################################

#######################################################################################################
#stations in rio validation
stations_name_RIO=[]
for i in range(0, data['stations/name'].shape[0]):      
    stations_name_RIO.append(data['stations/name'][i].decode('utf-8')[:2]+'0'+data['stations/name'][i].decode('utf-8')[2:]) 

p=Proj("+proj=lcc +lat_1=46.24470138549805 +lat_2=46.24470138549805 +lat_0=46.24470138549805 +lon_0=17.0 +x_0=0.0 +y_0=0.0 +a=6370000.0 +b=6370000.0 +units=m +no_defs")
p2=Proj("+init=EPSG:3035")

###########################################

element_data=element.upper()
if element.upper()=='PM25':
   element_data='PM2.5' 


none_list=[]
for i in range (0,365):
    none_list.append(np.nan)
none_list=np.array(none_list)     


zoznam=[]
st_frame=pd.DataFrame(columns=['list of stations (EEA)', 'lon (EEA)', 'lat (EEA)', 'type','coverage %','rio name','lon (rio)-lon (EEA)', 'lat (rio)-lat (EEA)'])
frame_hist=pd.DataFrame(columns=['site', 'BIAS_CMAQ', 'corr_CMAQ', 'RMSE_CMAQ', 'BIAS_RIO', 'corr_RIO', 'RMSE_RIO'])
frame_hist_y=pd.DataFrame(columns=['site', 'BIAS_CMAQ', 'BIAS_RIO'])
krajiny=['CZ','PL','SK']
ll=0
pom=0

with open('/data/rio/{0}/stations_{0}_daily.csv'.format(element), 'wt') as t, open('/data/rio/{0}/stations_{0}_annual.csv'.format(element), 'wt') as y:
      writert = csv.writer(t)
      writert.writerow( ('site','date','obser','mod','country','group'))  
      writery = csv.writer(y)
      writery.writerow( ('site','date','obser','mod','country','group'))  
      for k in krajiny:
          print(k)
          stanice=pd.read_csv('/media/sf_Share/{0}_AQeReporting_2013-2015/{0}_2013-2015_metadata.csv'.format(k),sep='\t', encoding='latin-1')
          data_eea=pd.read_csv('/media/sf_Share/{0}_AQeReporting_2013-2015/{0}_{1}_2013-2015_timeseries.csv'.format(k,subor), sep='\t', encoding='latin-1')
          for i in range(0,stanice.index.size):
              if stanice.AirPollutant[i] == element_data:
                 if stanice.AirQualityStationEoICode[i] not in zoznam:
                       
                       name_sta=stanice.AirQualityStationEoICode[i]
                       lon_sta=stanice['Longitude'][i]
                       lat_sta=stanice['Latitude'][i]
                       
                       if name_sta=='SK0264A':
                          name_sta='SK0015A'
                              
                       if name_sta=='SK0263A':
                          name_sta='SK0236A'
                        
                       zoznam.append(name_sta)
                       #pocita indexy i,j stanice a najblizsie a okolite indexy mriezky pre stanicu             
                        
                       ind_Small=bi_in2.indices(grid_CMAQ,lon_sta,lat_sta)                              
                       
                        # iba mala domena
                       if ind_Small[2] in range(0,100) and ind_Small[3] in range(0,178):
                              
                               if name_sta in stations_name_RIO:
                                  ind=stations_name_RIO.index(name_sta)
                                  name_rio=stations_name_RIO[ind]
                                  pom=pom+1
                                  lon_rio,lat_rio=p2(data['stations/x'][ind],data['stations/y'][ind],inverse=True)
                                  delta_lon=lon_rio-stanice['Longitude'][i]
                                  delta_lat=lat_rio-stanice['Latitude'][i]
                                  
                               else:
                                  name_rio='mi0ssing'
                                  delta_lon='none'
                                  delta_lat='none'
                               
                               pomoc=data_eea['AirQualityStation'] == stanice.AirQualityStation[i]                          
                               data_conc=data_eea[pomoc]
                               data_conc.index = pd.to_datetime(data_conc.DatetimeBegin) 
                               data_conc.sort_index(inplace=True)
                               data_conc=data_conc[(data_conc.index >'2015-01-01') & (data_conc.index < '2016-01-01')]
                               data_conc = data_conc.reindex(pd.date_range("2015-01-01 00:00:00", "2015-12-31 23:00:00" , freq='H'))
                               data_conc['modelCMAQ'] = cmaq_hourly[:,ind_Small[0],ind_Small[1]]
                              
                               
                               dayly_summary = pd.DataFrame()
                               dayly_summary['modelCMAQ'] = data_conc.modelCMAQ.resample('D').mean()
                               dayly_summary['Concentration'] = data_conc.Concentration.resample('D').mean()
                               dayly_summary['model_rio'] = rio_daily[ind_Small[0],ind_Small[1],:]
                               if name_sta in stations_name_RIO:
                                  dayly_summary['stanice_rio']=data['stations/value'][ind][:]
                               else:
                                  dayly_summary['stanice_rio']=none_list[:]
                                
                               dayly_summary=dayly_summary.replace(-9999.0, np.nan) 
                               
                               coverage=dayly_summary.count(numeric_only=True)[1]/3.65
                           
                               
                               
                               if coverage > 0 :
                                   

                                  
                                   for j in range(0,dayly_summary['modelCMAQ'].size):
                                       writert.writerow((name_sta,dayly_summary.index[j],dayly_summary['Concentration'][j],dayly_summary['modelCMAQ'][j], k,'CMAQ'))
                                   for j in range(0,dayly_summary['modelCMAQ'].size):    
                                       writert.writerow((name_sta,dayly_summary.index[j],dayly_summary['Concentration'][j],dayly_summary['model_rio'][j], k,'RIO'))
                                   
                                                                      
                                  
                                   
                                   BIAS_CMAQ=np.mean(dayly_summary['modelCMAQ']-dayly_summary['Concentration'])
                                   corr_CMAQ=dayly_summary['modelCMAQ'].corr(dayly_summary['Concentration'])  
                                   RMSE_CMAQ=np.sqrt(np.mean((dayly_summary['modelCMAQ']-dayly_summary['Concentration'])**2))  
                                   
                                   BIAS_RIO=np.mean(dayly_summary['model_rio']-dayly_summary['Concentration'])
                                   corr_RIO=dayly_summary['model_rio'].corr(dayly_summary['Concentration'])  
                                   RMSE_RIO=np.sqrt(np.mean((dayly_summary['model_rio']-dayly_summary['Concentration'])**2))  
                                   
                                   
                                   year_summary = pd.DataFrame()
                                   year_summary['modelCMAQ'] = data_conc.modelCMAQ.resample('A').mean()
                                   year_summary['model_rio'] = dayly_summary['model_rio'].resample('A').mean()
                                   year_summary['Concentration'] = data_conc.Concentration.resample('A').mean()
                                   
                                   BIAS_CMAQ_y=np.mean(year_summary['modelCMAQ']-year_summary['Concentration'])
                                   
                                   BIAS_RIO_y=np.mean(year_summary['model_rio']-year_summary['Concentration'])
                                   
                                   
                                   writery.writerow((name_sta,year_summary.index[0],year_summary['Concentration'][0],year_summary['modelCMAQ'][0], k,'CMAQ'))
                                   writery.writerow((name_sta,year_summary.index[0],year_summary['Concentration'][0],year_summary['model_rio'][0], k,'RIO'))
                                   
                                   
                                   st_frame.loc[ll]=[stanice.AirQualityStationEoICode[i],stanice['Longitude'][i],stanice['Latitude'][i],'{0}-{1}'.format(stanice.AirQualityStationArea[i],stanice.AirQualityStationType[i]),coverage,name_rio[:2]+name_rio[3:], delta_lon, delta_lat]
                                   frame_hist.loc[ll]=[stanice.AirQualityStationEoICode[i],BIAS_CMAQ,corr_CMAQ,RMSE_CMAQ,BIAS_RIO,corr_RIO,RMSE_RIO]
                                   frame_hist_y.loc[ll]=[stanice.AirQualityStationEoICode[i],BIAS_CMAQ_y,BIAS_RIO_y]
                                   ll=ll+1                                   
                                   
                                                                                                 
                                                                     
                                   
                                   
                                   
                                   plt.rcParams['figure.figsize'] = 30,10
                                   fig, ax1 = plt.subplots()
                                   ax1.set_ylabel('{0} [$\mu g/m^3$]'.format(element))
                                   ax1.set_title('{0}, {1}-{2}'.format(name_sta,stanice.AirQualityStationType[i],stanice.AirQualityStationArea[i]))
                                   ax1.yaxis.label.set_color('black')
                                   ax1.tick_params(axis='x',colors='black')
                                   ax1.tick_params(axis='y',colors='black')
                                   plt.plot(dayly_summary.index, dayly_summary['Concentration'],'-s',color='r',label=r'DATA') 
                                   plt.plot(dayly_summary.index, dayly_summary['modelCMAQ'],'-s',color='blue',label=r'CMAQ: BIAS={0:.2f}, corr={1:.2f}, RMSE={2:.2f}'.format(BIAS_CMAQ,corr_CMAQ,RMSE_CMAQ)) 
                                   plt.plot(dayly_summary.index, dayly_summary['model_rio'],'-s',color='y',label=r'RIO: BIAS={0:.2f}, corr={1:.2f}, RMSE={2:.2f}'.format(BIAS_RIO,corr_RIO,RMSE_RIO)) 
                                   
                                   plt.legend(title='coverage {0:.1f} %'.format(coverage))
                                   plt.savefig('/data/rio/{0}/time_series_individual_stations/{1}'.format(element,name_sta), dpi=300, bbox_inches='tight')
                                   plt.close()
                                   
                                   print(name_sta)


                             
######################################################################################################################################################################## 
#
#                                 
#    producing histograms
#                          
#                         
#########################################################################################################################################################################


plt.rcParams['figure.figsize'] = 40,10
frame_hist.plot.bar(x='site',y=['BIAS_CMAQ','BIAS_RIO']) 
plt.savefig('/data/rio/{0}/histograms/histogram_BIAS_daily_{0}'.format(element), dpi=300, bbox_inches='tight')
plt.close()

frame_hist.plot.bar(x='site',y=['corr_CMAQ','corr_RIO']) 
plt.savefig('/data/rio/{0}/histograms/histogram_corr_daily_{0}'.format(element), dpi=300, bbox_inches='tight')
plt.close()


frame_hist.plot.bar(x='site',y=['RMSE_CMAQ','RMSE_RIO']) 
plt.savefig('/data/rio/{0}/histograms/histogram_RMSE_daily_{0}'.format(element), dpi=300, bbox_inches='tight')
plt.close()


frame_hist_y.plot.bar(x='site',y=['BIAS_CMAQ','BIAS_RIO']) 
plt.savefig('/data/rio/{0}/histograms/histogram_BIAS_annual_{0}'.format(element), dpi=300, bbox_inches='tight')
plt.close()

######################################################################################################################################################################## 
#
#                                 
# producing annual maps   
#                          
#                         
#########################################################################################################################################################################



from mpl_toolkits.basemap import Basemap
plt.rcParams['figure.figsize'] = 15,8


lon=np.array(grid_CMAQ.variables['LON'][0,0,:,:])
lat=np.array(grid_CMAQ.variables['LAT'][0,0,:,:])
lon=lon[1:102,1:180]
lat=lat[1:102,1:180]
alt=np.array(grid_CMAQ.variables['HT'][0,0,:,:])
alt=alt[1:102,1:180]



meridians = np.arange(10.,35.,5.)
pararels = np.arange(45.,52.,1.)

levels=[0.7,1,5,10,15,20,25,30,35,40,46] 
mapb=Basemap(projection='lcc',lat_1=46.24470138549805,lat_2=46.24470138549805,lat_0=49.375,lon_0=17.0,width=833780,height=466351,resolution='i')
mapb.drawcountries()
mapb.drawmeridians(meridians,labels=[False,True,True, True, False])
mapb.drawparallels(pararels,labels=[True,True,True, True,True,True])
mapb.contourf(lon,lat,cmaq_ann,levels,cmap=plt.cm.jet,latlon=True) 

plt.colorbar(label='$\mu g/m^3$')
plt.title('Annual conc. CMAQ in $\mu g/m^3$')
plt.xlabel('PM$_{2.5}$')
plt.savefig('/data/rio/{0}/annual_maps/annual_conc_CMAQ_{0}'.format(element), dpi=300, bbox_inches='tight')
plt.close()

 
mapb=Basemap(projection='lcc',lat_1=46.24470138549805,lat_2=46.24470138549805,lat_0=49.375,lon_0=17.0,width=833780,height=466351,resolution='i')
mapb.drawcountries()
mapb.drawmeridians(meridians,labels=[False,True,True, True, False])
mapb.drawparallels(pararels,labels=[True,True,True, True,True,True])
mapb.contourf(lon,lat,rio_ann,levels,cmap=plt.cm.jet,latlon=True) 

plt.colorbar(label='$\mu g/m^3$')
plt.title('Annual conc. RIO in $\mu g/m^3$')
plt.xlabel('PM$_{2.5}$')
plt.savefig('/data/rio/{0}/annual_maps//annual_conc_RIO_{0}'.format(element), dpi=300, bbox_inches='tight')
plt.close()

mapb=Basemap(projection='lcc',lat_1=46.24470138549805,lat_2=46.24470138549805,lat_0=49.375,lon_0=17.0,width=833780,height=466351,resolution='i')
mapb.drawcountries()
mapb.drawmeridians(meridians,labels=[False,True,True, True, False])
mapb.drawparallels(pararels,labels=[True,True,True, True,True,True])
mapb.contourf(lon,lat,(rio_ann+cmaq_ann)/2,levels,cmap=plt.cm.jet,latlon=True) 

plt.colorbar(label='$\mu g/m^3$')
plt.title('Average of CMAQ and RIO in $\mu g/m^3$')
plt.xlabel('PM$_{2.5}$')
plt.savefig('/data/rio/{0}/annual_maps/annual_conc_CMAQ_RIO_average_{0}'.format(element), dpi=300, bbox_inches='tight')
plt.close()


levels=[-24,-20,-12,-10,-5,-2,0,2,5,7,8,10,15,20,25,30,35] 
mapb=Basemap(projection='lcc',lat_1=46.24470138549805,lat_2=46.24470138549805,lat_0=49.375,lon_0=17.0,width=833780,height=466351,resolution='i')
mapb.drawcountries()
mapb.drawmeridians(meridians,labels=[False,True,True, True, False])
mapb.drawparallels(pararels,labels=[True,True,True, True,True,True])
mapb.contourf(lon,lat,annual_dif,levels,cmap=plt.cm.jet,latlon=True) 

plt.colorbar(label='$\mu g/m^3$')
plt.title('Annual diff. CMAQ-RIO in $\mu g/m^3$')
plt.xlabel('PM$_{2.5}$')
plt.savefig('/data/rio/{0}/annual_maps/annual_diff_CMAQ-RIO_average_{0}'.format(element), dpi=300, bbox_inches='tight')
plt.close()

levels=[-87,-80,-70,-60,-50,-40,-30,-20,-10,-5,0,5,10,20,30,50,60,100,243,520]  
mapb=Basemap(projection='lcc',lat_1=46.24470138549805,lat_2=46.24470138549805,lat_0=49.375,lon_0=17.0,width=833780,height=466351,resolution='i')
mapb.drawcountries()
mapb.drawmeridians(meridians,labels=[False,True,True, True, False])
mapb.drawparallels(pararels,labels=[True,True,True, True,True,True])
mapb.contourf(lon,lat,annual_dif_per,levels,cmap=plt.cm.jet,latlon=True) 

plt.colorbar(label='%')
plt.title('Annual diff. (CMAQ-RIO)/RIO in %')
plt.xlabel('PM$_{2.5}$')
plt.savefig('/data/rio/{0}/annual_maps/annual_diff_CMAQ-RIO_percentage_{0}'.format(element), dpi=300, bbox_inches='tight')
plt.close()



levels=[-87,-10,-5,5,10,100,500]  
colorsp=['navy','blue','deepskyblue','mediumspringgreen','darkgreen','darksalmon','red' ]
mapb=Basemap(projection='lcc',lat_1=46.24470138549805,lat_2=46.24470138549805,lat_0=49.375,lon_0=17.0,width=833780,height=466351,resolution='i')
mapb.drawcountries()
mapb.drawmeridians(meridians,labels=[False,True,True, True, False])
mapb.drawparallels(pararels,labels=[True,True,True, True,True,True])
mapb.contourf(lon,lat,annual_dif_per,levels,colors=colorsp,latlon=True) 

plt.colorbar(label='%')
plt.title('Annual diff. (CMAQ-RIO)/RIO in %')
plt.xlabel('PM$_{2.5}$')
plt.savefig('/data/rio/{0}/annual_maps/annual_diff_CMAQ-RIO_percentage_{0}'.format(element), dpi=300, bbox_inches='tight')
plt.close()

levels=[-87,-70,-50,-30,-20,-10,-5,5,10,20,30,40,50,100]  
mapb=Basemap(projection='lcc',lat_1=46.24470138549805,lat_2=46.24470138549805,lat_0=49.375,lon_0=17.0,width=833780,height=466351,resolution='i')
mapb.drawcountries()
mapb.drawmeridians(meridians,labels=[False,True,True, True, False])
mapb.drawparallels(pararels,labels=[True,True,True, True,True,True])
mapb.contourf(lon,lat,annual_dif_per,levels,cmap=plt.cm.jet,latlon=True) 

plt.colorbar(label='%')
plt.title('Annual diff. (CMAQ-RIO)/RIO in %')
plt.xlabel('PM$_{2.5}$')
plt.savefig('/data/rio/{0}/annual_maps/annual_diff_CMAQ-RIO_percentage_{0}'.format(element), dpi=300, bbox_inches='tight')
plt.close()



#####################################################################################################################################################################






































#inProj = Proj("+init=EPSG:3035")
#outProj = Proj("+proj=lcc +lat_1=46.24470138549805 +lat_2=46.24470138549805 +lat_0=46.24470138549805 +lon_0=17.0 +x_0=0.0 +y_0=0.0 +a=6371229 +b=6371229 +units=m +no_defs")
#x1,y1 = np.array(grid['X'][:]),np.array(grid['Y'][:]),
#x2,y2 = transform(inProj,outProj,x1,y1)
#lonS, latS = outProj(x2, y2, inverse=True)
##lon2, lat2 = inProj(x1, y1, inverse=True)
#for i in range(0, data['stations/name'].shape[0]):
#      print(data['stations/name'][i])
#      print('lon',lonS[i])
#      print('lon',lon2[i])
#      print('lat',latS[i])
#      print('lat',lat2[i])







