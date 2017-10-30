import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#### DATA TRANSFORMATION

column_names = ['fico', 'frst_pay_dt', 'maturity_dt', 'msa_code', 'mi_pct', 'units', 'occupy_sts',
                'cltv', 'dti', 'orig_upb', 'ltv', 'interest_rate', 'channel', 'ppm_penalty', 'prod_type', 'state', 'property_type',
               'zipcode', 'id_loan', 'purpose', 'orgi_loan_term', 'num_borrowers', 'seller', 'servicer', 'month_report_period',
               'current_upb', 'delinquency_sts', 'loan_age', 'remain_months', 'current_interest_rate', 'non_interest_brng_upb']
single_family = pd.read_csv('single_family_cleaned.csv')
single_family.columns = column_names

# drop useless columns
# 'current_interest_rate': overlap with 'interest_rate'
# 'msa_code': use zip code as geomatric features
# 'ppm_penalty', 'prod_type': there is only one single value
# 'loan_age': this feature increases every month
# 'remain_month': this feature decreases every month

print 'drop useless columns'
print 'current_interest_rate: overlap with interest_rate'
print 'msa_code: use zip code as geomatric features'
print 'ppm_penalty, prod_type: there is only one single value'
print 'loan_age: this feature increases every month'
print 'remain_month: this feature decreases every month'

single_family_col_drop = single_family.drop(['current_interest_rate', 'msa_code','ppm_penalty', 'prod_type',
                                             'loan_age', 'remain_months'], axis=1)

## transform current_upb in every month into corresponding column
others = single_family_col_drop.drop(['month_report_period', 'current_upb'], axis=1)
month_upb = single_family_col_drop[['id_loan', 'month_report_period', 'current_upb']]

id_loans = list(month_upb.id_loan.unique())
months = list(month_upb.month_report_period.unique())

month_upb_transform = month_upb.pivot(columns='month_report_period', index='id_loan', values='current_upb').fillna(0)


new_names = ['current_upb_{}'.format(month) for month in months]
month_upb_transform.columns = sorted(new_names)

single_family_single_record = pd.merge(month_upb_transform.reset_index(), others.drop_duplicates(), on='id_loan')

single_family_single_record.delinquency_sts = single_family_single_record.delinquency_sts.apply(str)

## transform zip code into latitude and longitude
zip_la_lo = pd.read_table('zip_la_lo.txt', usecols=[0, 5,6], names=['zipcode', 'latitude', 'longitude'])
latitude = []
longitude = []
zip_la_lo.zipcode = zip_la_lo.zipcode//100*100
for cd in list(zip_la_lo.zipcode.unique()):
    latitude.append(np.mean(zip_la_lo[zip_la_lo.zipcode==cd].latitude))
    longitude.append(np.mean(zip_la_lo[zip_la_lo.zipcode==cd].longitude))
zip_la_lo_new = pd.DataFrame({'zipcode': list(zip_la_lo.zipcode.unique()),
                             'latitude': latitude,
                             'longitude': longitude})

data_la_lo = pd.merge(single_family_single_record, zip_la_lo_new, how='left', on='zipcode')

data_export = data_la_lo.drop(['id_loan', 'zipcode'], axis=1)

data_export.to_csv('single_family_single_record.csv', index=False)
