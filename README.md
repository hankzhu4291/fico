# fico
Predict the FICO score level for single family on a fixed rate mortgage

## Data scource
Origination and Performation:
http://www.freddiemac.com/research/datasets/sf_loanlevel_dataset.html

**Credential**:
Login: zhu429142416@gmail.com
Password: s:Ow{^{1

### transform zip code to latitude & longitude
https://www.census.gov/geo/maps-data/data/gazetteer2016.html

## Data Description
two main data tables: Origination data file(origin) and Monthly performance data file(perform). The two sets of data are connected by 'id_loan'

## Summary
### Data Cleaning process
1. remove features with over 50% NaN values:
  * origin: 'flag_fthb', 'flag_sc'
  * perform:  'repch_flag', 'flag_mod', 'cd_zero_bal', 'dt_zero_bal', 'dt_lst_pi',
         'mi_recoveries', 'net_sale_proceeds', 'non_mi_recoveries',
         'expenses', 'legal_costs', 'maint_pres_costs', 'taxes_ins_costs',
         'misc_costs', 'actual_loss', 'modcost'

2. remove rows with NaN values

## Prerequisites
Language: Python 2.7

## Running the script
```
cd fico
```

```
python run.py
```

## Author
**Hang Zhu**
