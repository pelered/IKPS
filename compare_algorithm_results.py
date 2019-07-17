import matplotlib.pyplot as plt
import create_models

"""
    Plot resulting array for comparison with original measuring
    
"""
############
#ovojeza double,2/3
#####################
double_time_izmjereni_X,double_time_izmjereni_Y=create_models.get_data_for_double_time(mode='data')
double_time_izmjereni=create_models.get_data_for_double_time(mode='result')
double_time_rezultat_nb=create_models.get_data_for_double_time(mode='nb')
double_time_rezultat_dtr=create_models.get_data_for_double_time(mode='dtr')
double_time_rezultat_dtc=create_models.get_data_for_double_time(mode='dtc')
double_time_rezultat_dtc_bin=create_models.get_data_for_double_time(mode='dtc_bin')

fig=plt.figure('Double time')
plt.plot(double_time_izmjereni, color='green', label='original')
plt.plot(double_time_rezultat_nb, color='skyblue', label='naive bayes')
plt.plot(double_time_rezultat_dtr, color='red', label='dt class')
plt.plot(double_time_rezultat_dtc, color='yellow', label='dt reg')

plt.axhline(y=300, color='black', linestyle='-')
plt.legend()
#plt.show()
fig.set_size_inches(18.5, 10.5,forward=True)
fig.savefig('Double time.png')


############################################################################################


###########################################################################################
#ovaj odlomak je leaeve one out
###########################################################################################

#ovo su bez slanoce suhi i bez suhih predvidanja, s leave one out verzijom

original_result_double_time_bez,original_result_double_time = create_models.get_data_for_original_leave_one(mode='result')
nb_results_original_bez,nb_results_original_sa = create_models.get_data_for_original_leave_one(mode='nb')
dtr_results_original_bez,dtr_results_original_sa = create_models.get_data_for_original_leave_one(mode='dtr')
dtc_results_original_bez,dtc_results_original_sa = create_models.get_data_for_original_leave_one(mode='dtc')
original_binarno_bez_leave,original_binarno_sa_leave=create_models.get_data_for_original_leave_one(mode='bin_result')
dtc_original_bin_bez_leave,dtc_original_bin_sa_leave=create_models.get_data_for_original_leave_one(mode='dtc_bin')


fig=plt.figure('Original data comparison prediction-bez suhih-leave')
plt.plot(original_result_double_time_bez, color='green', label='original')
plt.plot(nb_results_original_bez, color='skyblue', label='naive bayes')
plt.plot(dtc_results_original_bez, color='red', label='dt class')
plt.plot(dtr_results_original_bez, color='yellow', label='dt reg')

plt.axhline(y=300, color='black', linestyle='-')
plt.legend()
#plt.show()
fig.set_size_inches(18.5, 10.5,forward=True)
fig.savefig('Original data comparison prediction-bez suhih-leave.png')

plt.figure('Original data-bez suhih-leave')
plt.axhline(y=300, color='black', linestyle='-')
plt.plot(original_result_double_time_bez)
#plt.show()

fig1=plt.figure('Original data comparison prediction-suhi-leave')
plt.plot(original_result_double_time, color='green', label='original')
plt.plot(nb_results_original_sa, color='skyblue', label='naive bayes')
plt.plot(dtr_results_original_sa, color='red', label='dt class')
plt.plot(dtc_results_original_sa, color='yellow', label='dt reg')
plt.axhline(y=300, color='black', linestyle='-')
plt.legend()
#plt.show()
fig1.set_size_inches(18.5, 10.5,forward=True)
fig1.savefig('Original data comparison prediction-suhi-leave.png')

plt.figure('Original data-suhi-leave')
plt.axhline(y=300, color='black', linestyle='-')
plt.plot(original_result_double_time)
#plt.show()

##########################################

#ovo su sa slanocom suhi i bez suhih predvidanja, s leave one out verzijom



original_result_slanoca_bez,original_result_slanoca = create_models.get_data_with_salinity_leave_one(mode='result')
nb_result_slanoca_bez,nb_result_slanoca = create_models.get_data_with_salinity_leave_one(mode='nb')
dtc_result_slanoca_bez,dtc_result_slanoca = create_models.get_data_with_salinity_leave_one(mode='dtc')
dtr_result_slanoca_bez,dtr_result_slanoca = create_models.get_data_with_salinity_leave_one(mode='dtr')
original_binarno_slanoca_bez_leave,original_binarno_sa_leave=create_models.get_data_with_salinity_leave_one(mode='bin_result')
dtc_original_bin_slanoca_bez_leave,dtc_original_bin_sa_leave=create_models.get_data_with_salinity_leave_one(mode='dtc_bin')


fig2=plt.figure('Prediction with salinity-bez suhih-leave one out')
plt.plot(original_result_slanoca_bez, color='green', label='original')
plt.plot(nb_result_slanoca_bez, color='skyblue', label='naive bayes')
plt.plot(dtc_result_slanoca_bez, color='red', label='dt class')
plt.plot(dtr_result_slanoca_bez, color='yellow', label='dt reg')
plt.axhline(y=300, color='black', linestyle='-')
plt.legend()
#plt.show()
fig2.set_size_inches(18.5, 10.5,forward=True)
fig2.savefig('Prediction with salinity-bez suhih-leave one out.png')

plt.figure('Original with salinity-bez suhih-leave one out')
plt.plot(original_result_slanoca_bez)
plt.axhline(y=300, color='black', linestyle='-')
plt.xlim(0,len(original_result_slanoca_bez)-1)
#plt.show()

fig=plt.figure('Prediction with salinity-suhi-leave one out')
plt.plot(original_result_slanoca, color='green', label='original')
plt.plot(nb_result_slanoca, color='skyblue', label='naive bayes')
plt.plot(dtc_result_slanoca, color='red', label='dt class')
plt.plot(dtr_result_slanoca, color='yellow', label='dt reg')
plt.axhline(y=300, color='black', linestyle='-')
plt.legend()
#plt.show()
fig.set_size_inches(18.5, 10.5,forward=True)
fig.savefig('Prediction with salinity-suhi-leave one out.png')

plt.figure('Original with salinity-suhi-leave one out')
plt.axhline(y=300, color='black', linestyle='-')
plt.plot(original_result_slanoca)
#plt.show()


#############################################################################################

#ovaj odlomak 1/3+2/3 posvecen
############################################################################################
#ovo je bez suhih i sa suhim, bez slanoce
original_result_double_time_bez,original_result_double_time = create_models.get_data_for_original_model(mode='result')
nb_result_double_time_bez,nb_result_double_time = create_models.get_data_for_original_model(mode='nb')
dtc_result_double_time_bez,dtc_result_double_time = create_models.get_data_for_original_model(mode='dtc')
dtr_result_double_time_bez,dtr_result_double_time = create_models.get_data_for_original_model(mode='dtr')
original_binarno_bez,original_binarno_sa=create_models.get_data_for_original_model(mode='result_bin')
dtc_original_bin_bez,dtc_original_bin_sa=create_models.get_data_for_original_model(mode='dtc_bin')

fig=plt.figure('Original data comparison prediction-bez suhih')
plt.plot(original_result_double_time_bez, color='green', label='original')
plt.plot(nb_result_double_time_bez, color='skyblue', label='naive bayes')
plt.plot(dtc_result_double_time_bez, color='red', label='dt class')
plt.plot(dtr_result_double_time_bez, color='yellow', label='dt reg')
plt.axhline(y=300, color='black', linestyle='-')
plt.legend()
#plt.show()
fig.set_size_inches(18.5, 10.5,forward=True)
fig.savefig('Original data comparison prediction-bez suhih.png')

plt.figure('Original data-bez suhih')
plt.plot(original_result_double_time_bez)
plt.axhline(y=300, color='black', linestyle='-')
#plt.show()

fig=plt.figure('Original data comparison prediction-suhi')
plt.plot(original_result_double_time, color='green', label='original')
plt.plot(nb_result_double_time, color='skyblue', label='naive bayes')
plt.plot(dtc_result_double_time, color='red', label='dt class')
plt.plot(dtr_result_double_time, color='yellow', label='dt reg')
plt.axhline(y=300, color='black', linestyle='-')
plt.legend()
#plt.show()
fig.set_size_inches(18.5, 10.5,forward=True)
fig.savefig('Original data comparison prediction-suhi.png')

plt.figure('Original data-suhi')
plt.plot(original_result_double_time)
plt.axhline(y=300, color='black', linestyle='-')
#plt.show()
########################################################
#sada za suhe i bezsuhih sa slanocom

original_result_slanoca_bez,original_result_slanoca = create_models.get_data_with_salinity(mode='result')
nb_result_slanoca_bez,nb_result_slanoca = create_models.get_data_with_salinity(mode='nb')
dtc_result_slanoca_bez,dtc_result_slanoca = create_models.get_data_with_salinity(mode='dtc')
dtr_result_slanoca_bez,dtr_result_slanoca = create_models.get_data_with_salinity(mode='dtr')
original_binarno_slanoca_bez,original_binarno_sa=create_models.get_data_with_salinity(mode='result_bin')
dtc_original_bin_slanoca_bez,dtc_original_bin_sa=create_models.get_data_with_salinity(mode='dtc_bin')


fig=plt.figure('Prediction with salinity-bez suhih')
plt.plot(original_result_slanoca_bez, color='green', label='original')
plt.plot(nb_result_slanoca_bez, color='skyblue', label='naive bayes')
plt.plot(dtc_result_slanoca_bez, color='red', label='dt class')
plt.plot(dtr_result_slanoca_bez, color='yellow', label='dt reg')
plt.axhline(y=300, color='black', linestyle='-')
plt.legend()
#plt.show()
fig.set_size_inches(18.5, 10.5,forward=True)
fig.savefig('Prediction with salinity-bez suhih.png')

plt.figure('Original with salinity-bez suhih')
plt.plot(original_result_slanoca_bez)
plt.xlim(0,len(original_result_slanoca_bez)-1)
plt.axhline(y=300, color='black', linestyle='-')
#plt.show()

fig=plt.figure('Prediction with salinity-suhi')
plt.plot(original_result_slanoca, color='green', label='original')
plt.plot(nb_result_slanoca, color='skyblue', label='naive bayes')
plt.plot(dtc_result_slanoca, color='red', label='dt class')
plt.plot(dtr_result_slanoca, color='yellow', label='dt reg')
plt.axhline(y=300, color='black', linestyle='-')
plt.legend()
#plt.show()
fig.set_size_inches(18.5, 10.5,forward=True)
fig.savefig('Prediction with salinity-suhi.png')

plt.figure('Original with salinity-suhi')
plt.plot(original_result_slanoca)
plt.axhline(y=300, color='black', linestyle='-')
#plt.show()
