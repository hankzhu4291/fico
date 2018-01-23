import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import tree


data_credit = pd.read_csv('./data/single_family_single_record.csv')

## check distribution of fico scores
plt.figure(figsize=(20,10))
sns.distplot(data_credit.fico)
plt.show()

y = list(data_credit.fico)
y_level = []
for i in y:
    if i >= 800:
        y_level.append('exceptional')
    elif i>=740:
        y_level.append('very_good')
    else:
        y_level.append('good')
data_credit['fico_level'] = y_level

data_credit.delinquency_sts = data_credit.delinquency_sts.apply(str)

category_feature = ['channel', 'state', 'property_type', 'purpose', 'occupy_sts','seller', 'servicer',  u'frst_pay_dt'
                   , u'num_borrowers','delinquency_sts',u'units']
numeric_feature = [ u'mi_pct',  u'cltv', u'dti',u'non_interest_brng_upb',
       u'orig_upb', u'ltv', u'interest_rate',u'orgi_loan_term',
           u'latitude', u'longitude']
current_upb = [u'current_upb_201502', u'current_upb_201503', u'current_upb_201504',
       u'current_upb_201505', u'current_upb_201506', u'current_upb_201507',
       u'current_upb_201508', u'current_upb_201509', u'current_upb_201510',
       u'current_upb_201511', u'current_upb_201512', u'current_upb_201601',
       u'current_upb_201602', u'current_upb_201603', u'current_upb_201604',
       u'current_upb_201605', u'current_upb_201606', u'current_upb_201607',
       u'current_upb_201608', u'current_upb_201609', u'current_upb_201610',
       u'current_upb_201611', u'current_upb_201612', u'current_upb_201701',
       u'current_upb_201702', u'current_upb_201703']

for feature in numeric_feature:
    plt.figure(figsize=(20,10))
    sns.boxplot(x='fico_level', y=feature, data=data_credit)
    plt.show()

print 'transform category variable into dummy variable'
data_export_dummy = pd.get_dummies(columns=category_feature, data=data_credit)
data_export_dummy.columns = [x.replace(',','_').replace(' ','_') for x in list(data_export_dummy.columns)]

data_export_dummy.to_csv('./data/data_extracted_feature.csv', index=False)
