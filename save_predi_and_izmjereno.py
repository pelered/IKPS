# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 03:59:21 2019

@author: Petra
"""

import create_models
import pandas as pd
import numpy as np


writer = pd.ExcelWriter('Rezultati.xlsx', engine='xlsxwriter')

######original 2/3+1/3 ,suhi-bez suhih,bez slanoce

original_result_double_time_bez,original_result_double_time = create_models.get_data_for_original_model(mode='result')
nb_results_original_bez,nb_results_original_sa = create_models.get_data_for_original_model(mode='nb')
dtr_results_original_bez,dtr_results_original_sa = create_models.get_data_for_original_model(mode='dtr')
dtc_results_original_bez,dtc_results_original_sa = create_models.get_data_for_original_model(mode='dtc')
original_binarno_bez,original_binarno_sa=create_models.get_data_for_original_model(mode='result_bin')
dtc_original_bin_bez,dtc_original_bin_sa=create_models.get_data_for_original_model(mode='dtc_bin')


original_izmjereno_bez = pd.DataFrame({'Izmjereni bez': original_result_double_time_bez})
original_nb_bez=pd.DataFrame({'Naivni Bayes bez':nb_results_original_bez})
original_dtr_bez=pd.DataFrame({'Decision Tree Regresion bez':dtr_results_original_bez})
original_dtc_bez=pd.DataFrame({'Decision Tree klasifikator bez':dtc_results_original_bez})
original_bin_bez=pd.DataFrame({'Binarno izmjereno':original_binarno_bez})
original_bin_dtc_bez=pd.DataFrame({'DTC binarno bez':dtc_original_bin_bez})

original_izmjereno_sa=pd.DataFrame({'Izmjereni sa suhim': original_result_double_time})
original_nb_sa=pd.DataFrame({'Naivni Bayes sa':nb_results_original_sa})
original_dtr_sa=pd.DataFrame({'Decision Tree Regresion sa':dtr_results_original_sa})
original_dtc_sa=pd.DataFrame({'Decision Tree klasifikator sa':dtc_results_original_sa})
original_bin_sa=pd.DataFrame({'Binarno izmjereno':original_binarno_sa})
original_bin_dtc_sa=pd.DataFrame({'DTC binarno sa':dtc_original_bin_sa})


original_izmjereno_bez.to_excel(writer, sheet_name='Sheet1',index=False)  # Default position, cell A1.
original_nb_bez.to_excel(writer, sheet_name='Sheet1',startcol=1,index=False)
original_dtr_bez.to_excel(writer, sheet_name='Sheet1',startcol=2,index=False)
original_dtc_bez.to_excel(writer, sheet_name='Sheet1',startcol=3,index=False)
original_bin_bez.to_excel(writer, sheet_name='Sheet1',startcol=4,index=False)
original_bin_dtc_bez.to_excel(writer, sheet_name='Sheet1',startcol=5,index=False)

original_izmjereno_sa.to_excel(writer, sheet_name='Sheet1', startcol=8,index=False)
original_nb_sa.to_excel(writer, sheet_name='Sheet1',startcol=9,index=False)
original_dtr_sa.to_excel(writer, sheet_name='Sheet1',startcol=10,index=False)
original_dtc_sa.to_excel(writer, sheet_name='Sheet1',startcol=11,index=False)
original_bin_sa.to_excel(writer, sheet_name='Sheet1',startcol=12,index=False)
original_bin_dtc_sa.to_excel(writer, sheet_name='Sheet1',startcol=13,index=False)


#######
####### original leave one out,suhi-bez suhih,bez slanoce


original_result_double_time_bez_leave,original_result_double_time_leave = create_models.get_data_for_original_leave_one(mode='result')
nb_results_original_bez_leave,nb_results_original_sa_leave = create_models.get_data_for_original_leave_one(mode='nb')
dtr_results_original_bez_leave,dtr_results_original_sa_leave = create_models.get_data_for_original_leave_one(mode='dtr')
dtc_results_original_bez_leave,dtc_results_original_sa_leave = create_models.get_data_for_original_leave_one(mode='dtc')
original_binarno_bez_leave,original_binarno_sa_leave=create_models.get_data_for_original_leave_one(mode='bin_result')
dtc_original_bin_bez_leave,dtc_original_bin_sa_leave=create_models.get_data_for_original_leave_one(mode='dtc_bin')


original_result_double_time_bez_leave=original_result_double_time_bez_leave.tolist()
original_result_double_time_leave=original_result_double_time_leave.tolist()
original_binarno_bez_leave,original_binarno_sa_leave=original_binarno_bez_leave.tolist(),original_binarno_sa_leave.tolist()

original_izmjereno_bez_leave = pd.DataFrame({'Izmjereni bez leave': original_result_double_time_bez_leave})
original_nb_bez_leave=pd.DataFrame({'Naivni Bayes bez':nb_results_original_bez_leave})
original_dtr_bez_leave=pd.DataFrame({'Decision Tree Regresion bez':dtr_results_original_bez_leave})
original_dtc_bez_leave=pd.DataFrame({'Decision Tree klasifikator bez':dtc_results_original_bez_leave})
original_bin_bez_leave=pd.DataFrame({'Binarno izmjereno':original_binarno_bez_leave})
original_bin_dtc_bez_leave=pd.DataFrame({'DTC binarno bez':dtc_original_bin_bez_leave})


original_izmjereno_sa_leave=pd.DataFrame({'Izmjereni sa suhim leave': original_result_double_time_leave})
original_nb_sa_leave=pd.DataFrame({'Naivni Bayes sa':nb_results_original_sa_leave})
original_dtr_sa_leave=pd.DataFrame({'Decision Tree Regresion sa':dtr_results_original_sa_leave})
original_dtc_sa_leave=pd.DataFrame({'Decision Tree klasifikator sa':dtc_results_original_sa_leave})
original_bin_sa_leave=pd.DataFrame({'Binarno izmjereno':original_binarno_sa_leave})
original_bin_dtc_sa_leave=pd.DataFrame({'DTC binarno sa':dtc_original_bin_sa_leave})

original_izmjereno_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,index=False)  # Default position, cell A1.
original_nb_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=1,index=False)
original_dtr_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=2,index=False)
original_dtc_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=3,index=False)
original_bin_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=4,index=False)
original_bin_dtc_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=5,index=False)

original_izmjereno_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41, startcol=8,index=False)
original_nb_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=9,index=False)
original_dtr_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=10,index=False)
original_dtc_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=11,index=False)
original_bin_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=12,index=False)
original_bin_dtc_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=13,index=False)
#######

#####################
# sa slanocom, bez suhih-sa suhim, 2/3+1/3


original_result_slanoca_bez,original_result_slanoca = create_models.get_data_with_salinity(mode='result')
nb_result_slanoca_bez,nb_result_slanoca = create_models.get_data_with_salinity(mode='nb')
dtc_result_slanoca_bez,dtc_result_slanoca = create_models.get_data_with_salinity(mode='dtc')
dtr_result_slanoca_bez,dtr_result_slanoca = create_models.get_data_with_salinity(mode='dtr')
original_binarno_slanoca_bez,original_binarno_slanoca_sa=create_models.get_data_with_salinity(mode='result_bin')
dtc_original_bin_slanoca_bez,dtc_original_bin_slanoca_sa=create_models.get_data_with_salinity(mode='dtc_bin')

original_izmjereno_slanoca_bez = pd.DataFrame({'Izmjereni slanoca bez': original_result_slanoca_bez})
original_nb_slanoca_bez=pd.DataFrame({'Naivni Bayes bez':nb_result_slanoca_bez})
original_dtr_slanoca_bez=pd.DataFrame({'Decision Tree Regresion bez':dtr_result_slanoca_bez})
original_dtc_slanoca_bez=pd.DataFrame({'Decision Tree klasifikator bez':dtc_result_slanoca_bez})
original_izmjereno_bin_slanoca_bez = pd.DataFrame({'Izmjereni bin slanoca bez': original_binarno_slanoca_bez})
original_dtc_bin_slanoca_bez = pd.DataFrame({'DTC bin': dtc_original_bin_slanoca_bez})



original_izmjereno_slanoca_sa=pd.DataFrame({'Izmjereni slanoca sa suhim': original_result_slanoca})
original_nb_slanoca_sa=pd.DataFrame({'Naivni Bayes sa':nb_result_slanoca})
original_dtr_slanoca_sa=pd.DataFrame({'Decision Tree Regresion sa':dtr_result_slanoca})
original_dtc_slanoca_sa=pd.DataFrame({'Decision Tree klasifikator sa':dtc_result_slanoca})
original_izmjereno_bin_slanoca_sa = pd.DataFrame({'Izmjereni bin slanoca sa': original_binarno_slanoca_sa})
original_dtc_bin_slanoca_sa = pd.DataFrame({'DTC bin': dtc_original_bin_slanoca_sa})


original_izmjereno_slanoca_bez.to_excel(writer, sheet_name='Sheet1',startcol=17,index=False)  # Default position, cell A1.
original_nb_slanoca_bez.to_excel(writer, sheet_name='Sheet1',startcol=18,index=False)
original_dtr_slanoca_bez.to_excel(writer, sheet_name='Sheet1',startcol=19,index=False)
original_dtc_slanoca_bez.to_excel(writer, sheet_name='Sheet1',startcol=20,index=False)
original_izmjereno_bin_slanoca_bez.to_excel(writer, sheet_name='Sheet1',startcol=21,index=False)
original_dtc_bin_slanoca_bez.to_excel(writer, sheet_name='Sheet1',startcol=22,index=False)

original_izmjereno_slanoca_sa.to_excel(writer, sheet_name='Sheet1', startcol=26,index=False)
original_nb_slanoca_sa.to_excel(writer, sheet_name='Sheet1',startcol=27,index=False)
original_dtr_slanoca_sa.to_excel(writer, sheet_name='Sheet1',startcol=28,index=False)
original_dtc_slanoca_sa.to_excel(writer, sheet_name='Sheet1',startcol=29,index=False)
original_izmjereno_bin_slanoca_sa.to_excel(writer, sheet_name='Sheet1',startcol=30,index=False)
original_dtc_bin_slanoca_sa.to_excel(writer, sheet_name='Sheet1',startcol=31,index=False)



#####################
# sa slanocom, bez suhih-sa suhim, leave one out

original_result_slanoca_bez_leave,original_result_slanoca_leave = create_models.get_data_with_salinity_leave_one(mode='result')
nb_result_slanoca_bez_leave,nb_result_slanoca_leave = create_models.get_data_with_salinity_leave_one(mode='nb')
dtc_result_slanoca_bez_leave,dtc_result_slanoca_leave = create_models.get_data_with_salinity_leave_one(mode='dtc')
dtr_result_slanoca_bez_leave,dtr_result_slanoca_leave = create_models.get_data_with_salinity_leave_one(mode='dtr')
original_binarno_slanoca_bez_leave,original_binarno_sa_leave=create_models.get_data_with_salinity_leave_one(mode='bin_result')
dtc_original_bin_slanoca_bez_leave,dtc_original_bin_sa_leave=create_models.get_data_with_salinity_leave_one(mode='dtc_bin')


original_result_slanoca_bez_leave,original_result_slanoca_leave=original_result_slanoca_bez_leave.tolist(),original_result_slanoca_leave.tolist()
original_binarno_slanoca_bez_leave,original_binarno_sa_leave=original_binarno_slanoca_bez_leave.tolist(),original_binarno_sa_leave.tolist()

original_izmjereno_slanoca_bez_leave = pd.DataFrame({'Izmjereni slanoca leave bez': original_result_slanoca_bez_leave})
original_nb_slanoca_bez_leave=pd.DataFrame({'Naivni Bayes bez':nb_result_slanoca_bez_leave})
original_dtr_slanoca_bez_leave=pd.DataFrame({'Decision Tree Regresion bez':dtr_result_slanoca_bez_leave})
original_dtc_slanoca_bez_leave=pd.DataFrame({'Decision Tree klasifikator bez':dtc_result_slanoca_bez_leave})
original_izmjereno_bin_slanoca_bez_leave = pd.DataFrame({'Izmjereni bin slanoca leave bez': original_binarno_slanoca_bez_leave})
original_dtc_bin_slanoca_bez_leave=pd.DataFrame({'DTC bin bez':dtc_original_bin_slanoca_bez_leave})


original_izmjereno_slanoca_sa_leave=pd.DataFrame({'Izmjereni slanoca leave sa suhim': original_result_slanoca_leave})
original_nb_slanoca_sa_leave=pd.DataFrame({'Naivni Bayes sa':nb_result_slanoca_leave})
original_dtr_slanoca_sa_leave=pd.DataFrame({'Decision Tree Regresion sa':dtr_result_slanoca_leave})
original_dtc_slanoca_sa_leave=pd.DataFrame({'Decision Tree klasifikator sa':dtc_result_slanoca_leave})
original_izmjereno_bin_slanoca_sa_leave = pd.DataFrame({'Izmjereni bin slanoca leave ': original_binarno_sa_leave})
original_dtc_bin_slanoca_sa_leave=pd.DataFrame({'DTC bin ':dtc_original_bin_sa_leave})

original_izmjereno_slanoca_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=17,index=False)  # Default position, cell A1.
original_nb_slanoca_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=18,index=False)
original_dtr_slanoca_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=19,index=False)
original_dtc_slanoca_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=20,index=False)
original_izmjereno_bin_slanoca_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=21,index=False)
original_dtc_bin_slanoca_bez_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=22,index=False)

original_izmjereno_slanoca_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41, startcol=26,index=False)
original_nb_slanoca_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=27,index=False)
original_dtr_slanoca_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=28,index=False)
original_dtc_slanoca_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=29,index=False)
original_izmjereno_bin_slanoca_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=30,index=False)
original_dtc_bin_slanoca_sa_leave.to_excel(writer, sheet_name='Sheet1',startrow=41,startcol=31,index=False)

writer.save()
