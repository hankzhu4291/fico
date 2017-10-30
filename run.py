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

import subprocess


## FICO score levels prediction workflow
print 'Start FICO score levels prediction'
print '################# DATA CLEANING #################'
import data_cleaning.py as data_cleaning

print '################# DATA TRANSFORMATION #################'
import data_transformation.py as data_transformation

print '################# EDA & feature extraction #################'
import eda_feature_extraction.py as eda_feature_extraction

print '################# feature selection #################'
import feature_selection.py as feature_selection

print '################# prediction #################'
import prediction.py as prediction
