d={}

d['REZZO_3_resHeat_15_85_merUc']={
'source_type':'A',
'type':'csv+shape',
'input_file':'/data/em/data/input/CzechRep/emiss_2015/R3res/ENERGO_N15-L85_mereneUcinnosti/r3bilzsj2015n_em_total_ref_uprEP.csv',
'shape_file':'/data/em/data/input/CzechRep/geom/zsj_2016_utf8.shp',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SRC_TYPE',
'source_id':'KOD_ZSJNUM',
'shape_id':'KOD_ZSJNUM',
'def_emis':{'SO2_t': 'SO2', 'NH3_t': 'NH3', 'CH4_t': 'CH4', 'CO_t': 'CO', 'NO2_t': 'NO2', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'BAP_t': 'BAP', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'As_t': 'PM2_5_AS', 'Cd_t': 'PM2_5_CD', 'Cr_t': 'PM2_5_CR', 'Cu_t': 'PM2_5_CU', 'Hg_t': 'HG', 'Ni_t': 'PM2_5_NI', 'Pb_t': 'PM2_5_PB', 'Se_t': 'PM2_5_SE', 'Zn_t': 'PM2_5_ZN', 'NOX_t': 'NOX'},
'emission_inventory':{202020101: 1002020201, 202020102: 1002020201, 2020202: 1002020202, 202020301: 1002020203, 202020302: 1002020203, 202020303: 1002020203, 202020304: 1002020203, 202020401: 1002020204, 202020402: 1002020204, 202020403: 1002020204},
'units':'t/year',
 }


d['REZZO_3_tech']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/CzechRep/emiss_2015/R3tech/emise_2015_R3tech_v2017-07-18_BENZ_uprEP_utf8.csv',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'lon',
'y':'lat',
'grid_dx':0.1,
'grid_dy':0.1,
'EPSG':4326,
'def_emis':{'PM_CPRM_t': 'PM_CPRM', 'NH3_t': 'NH3', 'BENZEN_t': 'BZN', 'NMBVOC_t': 'NMBVOC', 'PM10_t': 'PM10', 'PM25_t': 'PM2_5_FPRM'},
'emission_inventory':{4: 1004000000, 5: 1005000000, 6: 1006000000, 9: 1009000000, 10: 10010000000},
'units':'t/year',
 }


d['REZZO_4_offroad']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/CzechRep/emiss_2016/offroad_mobile/r4_nesilnicni_500x500_bezlet.csv',
'sep':',',
'encoding':'utf-8',
'one_cat':8000000,
'x':'X_COORD',
'y':'Y_COORD',
'grid_dx':500,
'grid_dy':500,
'EPSG':28403,
'def_emis':{'NOx [kt/y]': 'NOX', 'NMVOC [kt/y]': 'NMVOC', 'SOx [kt/y]': 'SO2', 'NH3 [kt/y]': 'NH3', 'PM25 [kt/y]': 'PM2_5', 'PM10 [kt/y]': 'PM10', 'BC [kt/y]': 'PM2_5_EC', 'CO [kt/y]': 'CO', 'BaP [t/y]': 'BAP'},
'units':'kilot/year',
 }


d['REZZO_4_ATEM_grid_all']={
'source_type':'A',
'type':'shape',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/road_transp_ATEM/grid_v2018-02-22_CHMI/ctv_all.shp',
'shape_id':'CISLO_N',
'one_cat':7000000,
'def_emis':{'NOX': 'NOX', 'NO2': 'NO2', 'CO': 'CO', 'SO2': 'SO2', 'NH3': 'NH3', 'CXHY': 'VOC', 'CH4': 'CH4', 'BENZ': 'BZN', 'BAP': 'BAP', 'PM': 'PM', 'PM10': 'PM10', 'PM2_5': 'PM2_5', 'PM2_5_EC': 'PM2_5_EC', 'PM2_5_OC': 'PM2_5_OC', 'PM2_5_SO4': 'PM2_5_SO4', 'PM2_5_NA': 'PM2_5_NA', 'PM2_5_FPRM': 'PM2_5_FPRM', 'PM_CPRM': 'PM_CPRM', 'AS': 'PM2_5_AS', 'CD': 'PM2_5_CD', 'NI': 'PM2_5_NI', 'PB': 'PM2_5_PB'},
'units':'t/year',
 }


d['REZZO_4_ATEM_road_all']={
'source_type':'L',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/road_transp_ATEM/road_v2018-02-22_CHMI/Road_transp_line_all.shp',
'def_emis':{'NOX': 'NOX', 'NO2': 'NO2', 'CO': 'CO', 'SO2': 'SO2', 'NH3': 'NH3', 'CXHY': 'VOC', 'CH4': 'CH4', 'BENZ': 'BZN', 'BAP': 'BAP', 'PM': 'PM', 'PM10': 'PM10', 'PM2_5': 'PM2_5', 'PM2_5_EC': 'PM2_5_EC', 'PM2_5_OC': 'PM2_5_OC', 'PM2_5_SO4': 'PM2_5_SO4', 'PM2_5_NA': 'PM2_5_NA', 'PM2_5_FPRM': 'PM2_5_FPRM', 'PM_CPRM': 'PM_CPRM', 'AS': 'PM2_5_AS', 'CD': 'PM2_5_CD', 'NI': 'PM2_5_NI', 'PB': 'PM2_5_PB'},
'one_cat':1007000000,
'units':'t/year',
 }


d['REZZO_1_2']={
'source_type':'P',
'type':'csv',
'input_file':'/data/em/data/input/CzechRep/emiss_2015/R1a2/emise_2015_R1a2_v2017-07-20_corr_C6H6_and_SNAP6_uprEP_utf8.csv',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP_num',
'x':'x_gauss',
'y':'y_gauss',
'def_heights':True,
'ID':'id',
'height':'vyska_vyd',
'diameter':'prumer',
'temperature':'teplota',
'velocity':'rychlost',
'EPSG':28403,
'def_emis':{'BaP_t': 'BAP', 'v_BZN_t': 'BZN', 'CO_t': 'CO', 'nh3_t': 'NH3', 'NMBVOC_t': 'NMBVOC', 'v_NO_t': 'NO', 'v_NO2_t': 'NO2', 'CPRM_t': 'PM_CPRM', 'rv_As_t': 'PM2_5_AS', 'rv_Cd_t': 'PM2_5_CD', 'Cr_t': 'PM2_5_CR', 'Cu_t': 'PM2_5_CU', 'BC_komb_t': 'PM2_5_EC', 'FPRM_t': 'PM2_5_FPRM', 'NA_TNO_t': 'PM2_5_NA', 'Ni_tot_t': 'PM2_5_NI', 'OC_TNO_t': 'PM2_5_OC', 'rv_Pb_t': 'PM2_5_PB', 'Se_t': 'PM2_5_SE', 'SO4_TNO_t': 'PM2_5_SO4', 'Zn_t': 'PM2_5_ZN', 'SO2_t': 'SO2', 'TZL_t': 'PM', 'v_PM10_t': 'PM10', 'v_PM25_t': 'PM2_5', 'Nox_t': 'NOX'},
'emission_inventory':{1: 1001000000, 2: 1002000000, 3: 1003000000, 4: 1004000000, 5: 1005000000, 6: 1006000000, 9: 1009000000},
'units':'t/year',
 }


d['REZZO_4_ATEM_tunnel_all']={
'source_type':'P',
'type':'shape',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/road_transp_ATEM/tunnel_v2018-02-22_CHMI/Road_transp_tunnel_all.shp',
'sep':';',
'encoding':'utf-8',
'one_cat':7000000,
'def_heights':True,
'ID':'ID',
'height':'HEIGHT_M',
'diameter':'DIAMETER_M',
'temperature':'TEMP_DEGC',
'velocity':'SPEED_M_S',
'def_emis':{'NOX': 'NOX', 'NO2': 'NO2', 'CO': 'CO', 'SO2': 'SO2', 'NH3': 'NH3', 'CXHY': 'VOC', 'CH4': 'CH4', 'BENZ': 'BZN', 'BAP': 'BAP', 'PM': 'PM', 'PM10': 'PM10', 'PM2_5': 'PM2_5', 'PM2_5_EC': 'PM2_5_EC', 'PM2_5_OC': 'PM2_5_OC', 'PM2_5_SO4': 'PM2_5_SO4', 'PM2_5_NA': 'PM2_5_NA', 'PM2_5_FPRM': 'PM2_5_FPRM', 'PM_CPRM': 'PM_CPRM', 'AS': 'PM2_5_AS', 'CD': 'PM2_5_CD', 'NI': 'PM2_5_NI', 'PB': 'PM2_5_PB'},
'units':'t/year',
 }


d['PRG_apt_anti_ice']={
'source_type':'A',
'type':'shape',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/letiste_ruzyne/data/LET_antiicing.shp',
'shape_id':'ROZMER',
'one_cat':8050250,
'def_emis':{'NOX_TROK': 'NOX', 'CO_TROK': 'CO', 'SO2_TROK': 'SO2', 'PM_TROK': 'PM', 'PM10_TROK': 'PM10', 'PM25_TROK': 'PM2_5', 'NO2_TROK': 'NO2', 'BAP_TROK': 'BAP', 'CXHY_TROK': 'NMVOC'},
'units':'t/year',
 }


d['PRG_apt_deicing']={
'source_type':'A',
'type':'shape',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/letiste_ruzyne/data/LET_deicing.shp',
'shape_id':'ROZMER',
'one_cat':8050250,
'def_emis':{'NOX_TROK': 'NOX', 'CO_TROK': 'CO', 'SO2_TROK': 'SO2', 'PM_TROK': 'PM', 'PM10_TROK': 'PM10', 'PM25_TROK': 'PM2_5', 'NO2_TROK': 'NO2', 'BAP_TROK': 'BAP', 'CXHY_TROK': 'NMVOC'},
'units':'t/year',
 }


d['PRG_apt_LTO_land']={
'source_type':'A',
'type':'shape',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/letiste_ruzyne/data/LET_letiste-drahy_pz.shp',
'shape_id':'ID',
'one_cat':8050200,
'def_emis':{'NOX_TROK': 'NOX', 'CO_TROK': 'CO', 'SO2_TROK': 'SO2', 'PM_TROK': 'PM', 'PM10_TROK': 'PM10', 'PM25_TROK': 'PM2_5', 'NO2_TROK': 'NO2', 'BAP_TROK': 'BAP', 'CXHY_TROK': 'NMVOC'},
'units':'t/year',
 }


d['PRG_apt_engine_test']={
'source_type':'A',
'type':'shape',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/letiste_ruzyne/data/LET_motzk.shp',
'shape_id':'ID',
'one_cat':8050230,
'def_emis':{'NOX_TROK': 'NOX', 'CO_TROK': 'CO', 'SO2_TROK': 'SO2', 'PM_TROK': 'PM', 'PM10_TROK': 'PM10', 'PM25_TROK': 'PM2_5', 'NO2_TROK': 'NO2', 'BAP_TROK': 'BAP', 'CXHY_TROK': 'NMVOC'},
'units':'t/year',
 }


d['PRG_apt_fueling']={
'source_type':'A',
'type':'shape',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/letiste_ruzyne/data/LET_staceni.shp',
'shape_id':'ID',
'one_cat':8050240,
'def_emis':{'NOX_TROK': 'NOX', 'CO_TROK': 'CO', 'SO2_TROK': 'SO2', 'PM_TROK': 'PM', 'PM10_TROK': 'PM10', 'PM25_TROK': 'PM2_5', 'NO2_TROK': 'NO2', 'BAP_TROK': 'BAP', 'CXHY_TROK': 'NMVOC'},
'units':'t/year',
 }


d['PRG_apt_ops_tech_b']={
'source_type':'A',
'type':'shape',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/letiste_ruzyne/data/LET_ops_tech_b.shp',
'shape_id':'ID',
'one_cat':8050261,
'def_emis':{'NOX_TROK': 'NOX', 'CO_TROK': 'CO', 'SO2_TROK': 'SO2', 'PM_TROK': 'PM', 'PM10_TROK': 'PM10', 'PM25_TROK': 'PM2_5', 'NO2_TROK': 'NO2', 'BAP_TROK': 'BAP', 'CXHY_TROK': 'NMVOC'},
'units':'t/year',
 }


d['PRG_apt_ops_tech_d']={
'source_type':'A',
'type':'shape',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/letiste_ruzyne/data/LET_ops_tech_d.shp',
'shape_id':'ID',
'one_cat':8050262,
'def_emis':{'NOX_TROK': 'NOX', 'CO_TROK': 'CO', 'SO2_TROK': 'SO2', 'PM_TROK': 'PM', 'PM10_TROK': 'PM10', 'PM25_TROK': 'PM2_5', 'NO2_TROK': 'NO2', 'BAP_TROK': 'BAP', 'CXHY_TROK': 'NMVOC'},
'units':'t/year',
 }


d['PRG_apt_L_air']={
'source_type':'P',
'type':'shape',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/letiste_ruzyne/data/LET_letiste-drahy_lz_L_jako_body_po100m.shp',
'encoding':'utf-8',
'one_cat':8050210,
'def_heights':True,
'ID': 'ID',
'height':'HEIGHT',
'diameter':'DIAM',
'temperature':'TEMP',
'velocity':'SPEED',
'def_emis':{'NOX_TROK': 'NOX', 'CO_TROK': 'CO', 'SO2_TROK': 'SO2', 'PM_TROK': 'PM', 'PM10_TROK': 'PM10', 'PM25_TROK': 'PM2_5', 'NO2_TROK': 'NO2', 'BAP_TROK': 'BAP', 'CXHY_TROK': 'NMVOC'},
'units':'t/year',
 }


d['PRG_apt_TO_air']={
'source_type':'P',
'type':'shape',
'shape_file':'/data/em/data/input/CzechRep/emiss_2016/letiste_ruzyne/data/LET_letiste-drahy_lz_TO_jako_body_po100m.shp',
'encoding':'utf-8',
'one_cat':8050220,
'def_heights':True,
'ID': 'ID',
'height':'HEIGHT',
'diameter':'DIAM',
'temperature':'TEMP',
'velocity':'SPEED',
'def_emis':{'NOX_TROK': 'NOX', 'CO_TROK': 'CO', 'SO2_TROK': 'SO2', 'PM_TROK': 'PM', 'PM10_TROK': 'PM10', 'PM25_TROK': 'PM2_5', 'NO2_TROK': 'NO2', 'BAP_TROK': 'BAP', 'CXHY_TROK': 'NMVOC'},
'units':'t/year',
 }


d['TNO_without_CZE_SK_SL_Malopolska']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/TNO/TNO_MACC_III_emissions_v1_1_2011_ID_dopocet_opravaTurow_A.txt',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'Lon',
'y':'Lat',
'grid_dx':0.125,
'grid_dy':0.0625,
'filter':["ISO3 != 'CZE'", "~(ISO3 == 'SVK' and SNAP == 2)"],
'mask_out':True,
'EPSG':4326,
'def_emis':{'NOX': 'NOX', 'CO': 'CO', 'SO2': 'SO2', 'PM_CRS': 'PM_CPRM', 'PM2_5_EC': 'PM2_5_EC', 'PM2_5_OC': 'PM2_5_OC', 'PM2_5_NA': 'PM2_5_NA', 'PM2_5_SO4': 'PM2_5_SO4', 'PM2_5_OTHR': 'PM2_5_FPRM', 'NMVOC': 'NMVOC', 'CH4': 'CH4', 'NH3': 'NH3', 'PM10': 'PM10', 'PM2_5': 'PM2_5'},
'emission_inventory':{1: 1000000, 2: 2000000, 3: 3000000, 4: 4000000, 34: 4000000, 5: 5000000, 6: 6000000, 7: 7000000, 71: 7100000, 72: 7200000, 73: 7300000, 74: 7400000, 75: 7500000, 8: 8000000, 9: 9000000, 10: 10000000},
'units':'tonne/year',
 }


d['TNO_without_CZE_SK_SL_Malopolska_p']={
'source_type':'P',
'type':'csv',
'input_file':'/data/em/data/input/TNO/TNO_MACC_III_emissions_v1_1_2011_ID_dopocet_opravaTurow_P.txt',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'Lon',
'y':'Lat',
'def_heights':False,
'ID': 'ID',
'filter':["ISO3 != 'CZE'", "~(ISO3 == 'SVK' and SNAP == 2)"],
'mask_out':True,
'EPSG':4326,
'def_emis':{'NOX': 'NOX', 'CO': 'CO', 'SO2': 'SO2', 'PM_CRS': 'PM_CPRM', 'PM2_5_EC': 'PM2_5_EC', 'PM2_5_OC': 'PM2_5_OC', 'PM2_5_NA': 'PM2_5_NA', 'PM2_5_SO4': 'PM2_5_SO4', 'PM2_5_OTHR': 'PM2_5_FPRM', 'NMVOC': 'NMVOC', 'CH4': 'CH4', 'NH3': 'NH3', 'PM10': 'PM10', 'PM2_5': 'PM2_5'},
'emission_inventory':{1: 1000000, 2: 2000000, 3: 3000000, 4: 4000000, 34: 4000000, 5: 5000000, 6: 6000000, 7: 7000000, 71: 7100000, 72: 7200000, 73: 7300000, 74: 7400000, 75: 7500000, 8: 8000000, 9: 9000000, 10: 10000000},
'units':'tonne/year',
 }


d['BaP_Europe_2015_A']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/TNO/BaP_emissions_SNAP1-8_2015_v2017-10-27_notALL_ID_A.asc',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'Lon',
'y':'Lat',
'grid_dx':0.125,
'grid_dy':0.0625,
'filter':["ISO3 != 'CZ'", "~(ISO3 == 'SK' and SNAP == 2)"],
'mask_out':True,
'EPSG':4326,
'def_emis':{'BaP_t': 'BAP'},
'emission_inventory':{1: 1000000, 2: 2000000, 3: 3000000, 4: 4000000, 5: 5000000, 6: 6000000, 7: 7000000, 8: 8000000, 9: 9000000, 10: 10000000},
'units':'t/year',
 }


d['BaP_Europe_2015_P']={
'source_type':'P',
'type':'csv',
'input_file':'/data/em/data/input/TNO/BaP_emissions_SNAP1-8_2015_v2017-10-27_notALL_ID_P.asc',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'Lon',
'y':'Lat',
'def_heights':'zero',
'filter':["ISO3 != 'CZ'", "~(ISO3 == 'SK' and SNAP == 2)"],
'mask_out':True,
'EPSG':4326,
'def_emis':{'BaP_t': 'BAP'},
'emission_inventory':{1: 1000000, 2: 2000000, 3: 3000000, 4: 4000000, 5: 5000000, 6: 6000000, 7: 7000000, 8: 8000000, 9: 9000000, 10: 10000000},
'units':'t/year',
 }


d['SVK_resHeat_15_85']={
'source_type':'A',
'type':'csv+shape',
'input_file':'/data/em/data/input/Slovakia/emiss_2015/res_heat/zsj_N15-L85/SK_2015_resHeat_N15-L85_all_fuels_NA_SO4_FPRM.csv',
'shape_file':'/data/em/data/input/Slovakia/geom/Slovakia_ZSJ_2015_asi_oprava.shp',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SRC_TYPE',
'source_id':'ZSJ',
'shape_id':'ZSJ_ID',
'def_emis':{'SO2_g': 'SO2', 'NH3_g': 'NH3', 'CH4_g': 'CH4', 'CO_g': 'CO', 'NOX_g': 'NOX', 'NMVOC_g': 'NMVOC', 'C6H6_g': 'BZN', 'BAP_mg': 'BAP', 'TSP_g': 'PM', 'PM10_g': 'PM10', 'PM2_5_g': 'PM2_5', 'BC_g': 'PM2_5_EC', 'OC_g': 'PM2_5_OC', 'NA_g': 'PM2_5_NA', 'SO4_g': 'PM2_5_SO4', 'FPRM_g': 'PM2_5_FPRM', 'AS_mg': 'PM2_5_AS', 'CD_mg': 'PM2_5_CD', 'CR_mg': 'PM2_5_CR', 'CU_mg': 'PM2_5_CU', 'HG_mg': 'HG', 'NI_mg': 'PM2_5_NI', 'PB_mg': 'PM2_5_PB', 'SE_mg': 'PM2_5_SE', 'ZN_mg': 'PM2_5_ZN'},
'emission_inventory':{202020101: 2002020201, 2020202: 2002020202, 202020301: 2002020203, 202020302: 2002020203, 202020303: 2002020203, 202020304: 2002020203, 202020401: 2002020204},
'units':'g/year',
 }


d['SVK_snap_02_point']={
'source_type':'P',
'type':'csv',
'input_file':'/data/em/data/input/Slovakia/emiss_2015/point_snap_2/SNAP2_point_NEIS_for_CHMI_1A4_v5_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':2002000000,
'x':'lon',
'y':'lat',
'def_heights':True,
'ID':'id',
'height':'outlt_hgt',
'diameter':'outlt_diam',
'temperature':'exh_t',
'velocity':'exh_vel',
'EPSG':4326,
'def_emis':{'tzl_m': 'PM', 'pm10_m': 'PM10', 'pm2_5_m': 'PM2_5', 'so2_m': 'SO2', 'nox_m': 'NOX', 'co_m': 'CO', 'nmvoc_m': 'NMBVOC', 'benzen_m': 'BZN', 'nh3_m': 'NH3'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_bochenski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_bochenski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_brzeski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_brzeski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_dabrowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_dabrowski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_gorlicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_gorlicki_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_chrzanowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_chrzanowski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_Krakow_city']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_Krakow_city_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_krakowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_krakowski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_limanowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_limanowski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_miechowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_miechowski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_myslenicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_myslenicki_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_nowosadecki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_nowosadecki_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_nowy_sacz_city']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_nowy_sacz_city_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_olkuski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_olkuski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_oswiecimski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_oswiecimski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_proszowicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_proszowicki_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_suski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_suski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_tarnowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_tarnowski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_tatrzanski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_tatrzanski_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_Tranow_city']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_Tranow_city_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_wadowicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_wadowicki_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR10_wielicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0010_wielicki_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_NR10']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_National_roads__0010_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_VR10']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Voivodeship_roads__0010_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_LR25']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Local_roads__0025_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_NR25']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_National_roads__0025_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_MP_roadTransp_VR25']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/road_transport/Emission_Voivodeship_roads__0025_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3107000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'PM2_5_EC_t': 'PM2_5_EC', 'PM2_5_OC_t': 'PM2_5_OC', 'PM2_5_NA_t': 'PM2_5_NA', 'PM2_5_SO4_t': 'PM2_5_SO4', 'PM2_5_FPRM_t': 'PM2_5_FPRM', 'BAP_PM10_t': 'BAP', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'CO_t': 'CO'},
'units':'t/year',
 }


d['POL_SL_roadTransp_kraj']={
'source_type':'L',
'shape_file':'/data/em/data/input/Poland/Silesia/emiss_2015/v2017-12-15/road_transport/baza_drogi_krajowe_emisja_SL_2015_CHMI_specPM.shp',
'def_emis':{'SO2_T': 'SO2', 'NOX_T': 'NOX', 'NO2_T': 'NO2', 'TSP_T': 'PM', 'PM10_T': 'PM10', 'PM2_5_T': 'PM2_5', 'PM2_5_EC_T': 'PM2_5_EC', 'PM2_5_OC_T': 'PM2_5_OC', 'PM2_5_NA_T': 'PM2_5_NA', 'PM2_5_SO4': 'PM2_5_SO4', 'PM2_5_FPRM': 'PM2_5_FPRM', 'BAP_PM10_T': 'BAP', 'NMVOC_T': 'NMVOC', 'BZN_T': 'BZN', 'CO_T': 'CO'},
'one_cat':3207000000,
'units':'t/year',
 }


d['POL_SL_roadTransp_woj']={
'source_type':'L',
'shape_file':'/data/em/data/input/Poland/Silesia/emiss_2015/v2017-12-15/road_transport/baza_drogi_wojewodzkie_emisja_SL_2015_CHMI_specPM.shp',
'def_emis':{'SO2_T': 'SO2', 'NOX_T': 'NOX', 'NO2_T': 'NO2', 'TSP_T': 'PM', 'PM10_T': 'PM10', 'PM2_5_T': 'PM2_5', 'PM2_5_EC_T': 'PM2_5_EC', 'PM2_5_OC_T': 'PM2_5_OC', 'PM2_5_NA_T': 'PM2_5_NA', 'PM2_5_SO4': 'PM2_5_SO4', 'PM2_5_FPRM': 'PM2_5_FPRM', 'BAP_PM10_T': 'BAP', 'NMVOC_T': 'NMVOC', 'BZN_T': 'BZN', 'CO_T': 'CO'},
'one_cat':3207000000,
'units':'t/year',
 }


d['POL_SL_roadTransp_PiG']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Silesia/emiss_2015/v2017-12-15/road_transport/baza_drogi_PiG_emisja_SL_2015_CHMI_utf8_specPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3207000000,
'x':'X_m',
'y':'Y_m',
'grid_dx':250,
'grid_dy':250,
'EPSG':2180,
'def_emis':{'SO2_T': 'SO2', 'NOX_T': 'NOX', 'NO2_T': 'NO2', 'TSP_T': 'PM', 'PM10_T': 'PM10', 'PM2_5_T': 'PM2_5', 'PM2_5_EC_T': 'PM2_5_EC', 'PM2_5_OC_T': 'PM2_5_OC', 'PM2_5_NA_T': 'PM2_5_NA', 'PM2_5_SO4': 'PM2_5_SO4', 'PM2_5_FPRM': 'PM2_5_FPRM', 'BAP_PM10_T': 'BAP', 'NMVOC_T': 'NMVOC', 'BZN_T': 'BZN', 'CO_T': 'CO'},
'units':'t/year',
 }


d['POL_MP_point']={
'source_type':'P',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/point/Point_emission_Malopolska_2015_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'lon_deg',
'y':'lat_deg',
'def_heights':True,
'ID':'ID',
'height':'height_m',
'diameter':'diameter_m',
'temperature':'temp_K',
'velocity':'speed_m_s',
'EPSG':4326,
'def_emis':{'TSP_kg': 'PM', 'PM10_kg': 'PM10', 'PM2_5_kg': 'PM2_5', 'SO2_kg': 'SO2', 'NOX_kg': 'NOX', 'NO2_kg': 'NO2', 'CO_kg': 'CO', 'NH3_kg': 'NH3', 'NMVOC_kg': 'NMVOC', 'BENZ_kg': 'BZN', 'BAP_kg': 'BAP', 'As_kg': 'PM2_5_AS', 'Cd_kg': 'PM2_5_CD', 'Hg_kg': 'HG', 'Pb_kg': 'PM2_5_PB', 'CH4_kg': 'CH4'},
'emission_inventory':{1: 3001000000, 2: 3002000000, 3: 3003000000, 4: 3004000000, 5: 3005000000, 6: 3006000000, 9: 3009000000, 10: 30010000000, 11: 30011000000},
'units':'kg/year',
 }


d['POL_SL_point']={
'source_type':'P',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Silesia/emiss_2015/v2017-12-15/point/baza_punktowa_emisja_SL_2015_v2018-03-02_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'cat_internal':'SNAP',
'x':'x_m',
'y':'y_m',
'def_heights':True,
'ID':'ID',
'height':'height_m',
'diameter':'diameter_m',
'temperature':'temp_K',
'velocity':'speed_m_s',
'EPSG':2180,
'def_emis':{'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'CO_t': 'CO', 'NH3_t': 'NH3', 'NMVOC_t': 'NMVOC', 'BENZ_t': 'BZN', 'BAP_t': 'BAP', 'CH4_t': 'CH4', 'As_t': 'PM2_5_AS', 'Cd_t': 'PM2_5_CD', 'Hg_t': 'HG'},
'emission_inventory':{1: 3001000000, 2: 3002000000, 3: 3003000000, 4: 3004000000, 5: 3005000000, 6: 3006000000, 8: 3008000000, 9: 3009000000, 10: 30010000000},
'units':'t/year',
 }


d['POL_MP_resHeat_15_85_10']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/res_heat/Emission_2015_R3res_Malopolska_N15-L85_CHMI_0010x0010_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3102020200,
'x':'lon_deg',
'y':'lat_deg',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'BAP_t': 'BAP', 'CO_t': 'CO', 'NMVOC_t': 'NMVOC', 'NH3_t': 'NH3', 'BENZ_t': 'BZN', 'As_t': 'PM2_5_AS', 'Cd_t': 'PM2_5_CD', 'CH4_t': 'CH4', 'Hg_t': 'HG'},
'units':'t/year',
 }


d['POL_MP_resHeat_15_85_25']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/res_heat/Emission_2015_R3res_Malopolska_N15-L85_CHMI_0025x0025_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3102020200,
'x':'lon_deg',
'y':'lat_deg',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'BAP_t': 'BAP', 'CO_t': 'CO', 'NMVOC_t': 'NMVOC', 'NH3_t': 'NH3', 'BENZ_t': 'BZN', 'As_t': 'PM2_5_AS', 'Cd_t': 'PM2_5_CD', 'CH4_t': 'CH4', 'Hg_t': 'HG'},
'units':'t/year',
 }


d['POL_SL_resHeat_15_85']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Silesia/emiss_2015/v2017-12-15/res_heat/Emission_2015_R3res_Silesia_N15-L85_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3202020200,
'x':'PUWG92_X',
'y':'PUWG92_Y',
'grid_dx':250,
'grid_dy':250,
'EPSG':2180,
'def_emis':{'SO2_t': 'SO2', 'NOX_t': 'NOX', 'NO2_t': 'NO2', 'TSP_t': 'PM', 'PM10_t': 'PM10', 'PM2_5_t': 'PM2_5', 'BAP_t': 'BAP', 'CO_t': 'CO', 'NMVOC_t': 'NMVOC', 'NH3_t': 'NH3', 'BENZ_t': 'BZN'},
'units':'t/year',
 }


d['POL_MP_unorg_10']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/unorganised/Unorganized_emission_urban_0010x0010_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30011000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'PM10_kg': 'PM10', 'PM2_5_kg': 'PM2_5'},
'units':'kg/year',
 }


d['POL_MP_unorg_25']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/unorganised/Unorganized_emission_zone_0025x0025_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30011000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_kg': 'PM10', 'PM2_5_kg': 'PM2_5'},
'units':'kg/year',
 }


d['POL_SL_unorg']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Silesia/emiss_2015/v2017-12-15/unorganised/baza_niezorganizowane_emisja_SL_2015_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30011000000,
'x':'X_m',
'y':'Y_m',
'grid_dx':250,
'grid_dy':250,
'EPSG':2180,
'def_emis':{'PM10_kg': 'PM10', 'PM2_5_kg': 'PM2_5'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_wadowicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/wadowicki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_bochenski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/bochenski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_brzeski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/brzeski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_chrzanowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/chrzanowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_dabrowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/dabrowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_gorlicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/gorlicki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_krakowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/krakowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_limanowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/limanowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_miechowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/miechowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_myslenicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/myslenicki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_nowosadecki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/nowosadecki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_nowotarski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/nowotarski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_olkuski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/olkuski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_oswiecimski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/oswiecimski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_proszowicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/proszowicki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_suski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/suski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_tarnowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/tarnowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_tatrzanski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/tatrzanski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_wielicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/wielicki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_machines_towns']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/towns_Crop_Production_Emission_CHMI_0010_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_towns']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/towns_Crop_Production_Emission_CHMI_0010_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_SL_agri_machines']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Silesia/emiss_2015/v2017-12-15/agriculture/baza_uprawy_rolnictwo_emisja_SL_2015_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':3008000000,
'x':'X_m',
'y':'Y_m',
'grid_dx':1000,
'grid_dy':1000,
'EPSG':2180,
'def_emis':{'TSP_8': 'PM', 'PM10_8': 'PM10', 'PM2_5_8': 'PM2_5', 'NOX_8': 'NOX', 'NO2_8': 'NO2', 'NMVOC_8': 'NMVOC', 'NH3_8': 'NH3', 'SO2_8': 'SO2', 'CO_8': 'CO'},
'units':'kg/year',
 }


d['POL_SL_agri_cf']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Silesia/emiss_2015/v2017-12-15/agriculture/baza_uprawy_rolnictwo_emisja_SL_2015_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'X_m',
'y':'Y_m',
'grid_dx':1000,
'grid_dy':1000,
'EPSG':2180,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_bochenski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/bochenski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_brzeski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/brzeski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_chrzanowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/chrzanowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_dabrowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/dabrowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_gorlicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/gorlicki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_krakowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/krakowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_limanowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/limanowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_miechowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/miechowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_myslenicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/myslenicki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_nowosadecki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/nowosadecki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_nowotarski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/nowotarski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_olkuski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/olkuski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_oswiecimski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/oswiecimski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_proszowicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/proszowicki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_suski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/suski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_tarnowski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/tarnowski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_tatrzanski']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/tatrzanski_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_wadowicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/wadowicki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_cf_wielicki']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/crop_2018-03-09/wielicki_district_Crop_Production_Emission_CHMI_0025_utf8_sumPM.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'PM10_10CF': 'PM10', 'PM2_5_10CF': 'PM2_5', 'NO_10F': 'NO', 'NMVOC_10F': 'NMBVOC', 'NH3_10F': 'NH3'},
'units':'kg/year',
 }


d['POL_SL_agri_livestock']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Silesia/emiss_2015/v2017-12-15/agriculture/baza_hodowla_rolnictwo_emisja_SL_2015_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'X_m',
'y':'Y_m',
'grid_dx':250,
'grid_dy':250,
'EPSG':2180,
'def_emis':{'TSP_kg': 'PM', 'PM10_kg': 'PM10', 'PM2_5_kg': 'PM2_5', 'NO_kg': 'NO', 'NMVOC_kg': 'NMBVOC', 'NH3_kg': 'NH3'},
'units':'kg/year',
 }


d['POL_MP_agri_livestock_urban']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/livestock/livestock_husbandry_emission_urban_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.001,
'grid_dy':0.001,
'EPSG':4326,
'def_emis':{'TSP_kg': 'PM', 'PM10_kg': 'PM10', 'PM2_5_kg': 'PM2_5', 'NO_kg': 'NO', 'NMVOC_kg': 'NMBVOC', 'NH3_kg': 'NH3', 'CH4_kg': 'CH4'},
'units':'kg/year',
 }


d['POL_MP_agri_livestock_zone']={
'source_type':'A',
'type':'csv',
'input_file':'/data/em/data/input/Poland/Malopolska/emiss_2015/v2017-12-15/agriculture/livestock/livestock_husbandry_emission_zone_CHMI_utf8.csv',
'sep':';',
'encoding':'utf-8',
'one_cat':30010000000,
'x':'grdCen_lon',
'y':'grdCen_lat',
'grid_dx':0.0025,
'grid_dy':0.0025,
'EPSG':4326,
'def_emis':{'TSP_kg': 'PM', 'PM10_kg': 'PM10', 'PM2_5_kg': 'PM2_5', 'NO_kg': 'NO', 'NMVOC_kg': 'NMBVOC', 'NH3_kg': 'NH3', 'CH4_kg': 'CH4'},
'units':'kg/year',
 }


