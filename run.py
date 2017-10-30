import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn import linear_model

from sklearn.metrics import confusion_matrix, classification_report
import xgboost as xgb

import os


## FICO score levels prediction workflow
print 'Start FICO score levels prediction'
print '################# DATA CLEANING #################'
os.system('data_cleaning.py')

print '################# DATA TRANSFORMATION #################'
os.system('data_transformation.py')

print '################# EDA & feature extraction #################'
os.sytem('eda_feature_extraction.py')

print '################# feature selection #################'
os.system('feature_selection.py')

print '################# prediction #################'
os.system('prediction.py')
