import numpy as np
import pandas as pd


#### DATA IMPORT
column_names_origin = ['fico','dt_first_pi','flag_fthb','dt_matr','cd_msa',"mi_pct",'cnt_units','occpy_sts','cltv'
,'dti','orig_upb','ltv','int_rt','channel','ppmt_pnlty','prod_type','st', 'prop_type','zipcode','id_loan','loan_purpose',
'orig_loan_term','cnt_borr','seller_name','servicer_name', 'flag_sc']
origin_q1 = pd.read_table('./data/historical_data1_Q12015.txt', names=column_names_origin, sep='|', na_values=['', ' ', '  ', '   '])
origin_q2 = pd.read_table('./data/historical_data1_Q22015.txt', names=column_names_origin, sep='|', na_values=['', ' ', '  ', '   '])
origin_q3 = pd.read_table('./data/historical_data1_Q32015.txt', names=column_names_origin, sep='|', na_values=['', ' ', '  ', '   '])
origin_q4 = pd.read_table('./data/historical_data1_Q42015.txt', names=column_names_origin, sep='|', na_values=['', ' ', '  ', '   '])

column_names_perform = ['id_loan','svcg_cycle','current_upb','delq_sts','loan_age','mths_remng',
'repch_flag','flag_mod', 'cd_zero_bal', 'dt_zero_bal','current_int_rt','non_int_brng_upb','dt_lst_pi','mi_recoveries',
'net_sale_proceeds','non_mi_recoveries','expenses', 'legal_costs',
'maint_pres_costs','taxes_ins_costs','misc_costs','actual_loss', 'modcost']
perform_q1 = pd.read_table('./data/historical_data1_time_Q12015.txt', names=column_names_perform, sep='|', na_values=['', ' ', '  ', '   '])
perform_q2 = pd.read_table('./data/historical_data1_time_Q22015.txt', names=column_names_perform, sep='|', na_values=['', ' ', '  ', '   '])
perform_q3 = pd.read_table('./data/historical_data1_time_Q32015.txt', names=column_names_perform, sep='|', na_values=['', ' ', '  ', '   '])
perform_q4 = pd.read_table('./data/historical_data1_time_Q42015.txt', names=column_names_perform, sep='|', na_values=['', ' ', '  ', '   '])

origin_2015 = pd.concat([origin_q1, origin_q2, origin_q3, origin_q4], ignore_index=True)
perform_2015 = pd.concat([perform_q1, perform_q2, perform_q3, perform_q4], ignore_index=True)

#### DATA CLEANING

## check nan percentage
def na_check(data):
    for i in range(data.shape[1]):
        print data.columns[i], float(list(data.iloc[:, i]).count(np.nan))/len(data)

na_check(origin_2015)
na_check(perform_2016)

## Remove columns with over 50% nan values
na_col_origin = ['flag_fthb', 'flag_sc']

na_col_perform = [ u'repch_flag', u'flag_mod', u'cd_zero_bal',
       u'dt_zero_bal', u'dt_lst_pi',
       u'mi_recoveries', u'net_sale_proceeds', u'non_mi_recoveries',
       u'expenses', u'legal_costs', u'maint_pres_costs', u'taxes_ins_costs',
       u'misc_costs', u'actual_loss', u'modcost']

print 'removed columns in origin data'
print 'flag_fthb', 'flag_sc'

print 'removed columns in performance data'
print na_col_perform

na_removed_data = pd.merge(origin_2015.drop(na_col_origin, axis=1), perform_2015.drop(na_col_perform, axis=1),
                           on='id_loan', how='right')
data_cleaned = na_removed_data.dropna()

print 'export cleaned data'
data_cleaned.to_csv('single_family_cleaned.csv', index=False)
