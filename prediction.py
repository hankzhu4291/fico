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


data_selected_feature = pd.read_csv('./data/data_selected_feature_class.csv')
X = data_selected_feature.drop('fico', axis=1)
y = data_selected_feature.fico

# transform data frame to sparse matrix
X_sparse = scipy.sparse.csr_matrix(X.values)
y_array = y.as_matrix()

# split data
X_train, X_test, y_train, y_test = train_test_split(X_sparse, y_array, test_size=0.2, random_state=112)

xgb_clf = xgb.XGBClassifier(random_state=123, n_jobs=-1, objective='multi:softmax', n_estimators=500, learning_rate=0.1)
xgb_clf.fit(X_train, y_train)

y_predict_xgb = xgb_clf.predict(X_test)

print 'prediction result from xgboost'
print confusion_matrix( y_test, y_predict_xgb)
print classification_report(y_pred=pd.Series(y_predict_xgb), y_true=pd.Series(y_test))
#              precision    recall  f1-score   support
#
# exceptional       0.47      0.02      0.04     31753
#        good       0.66      0.49      0.56     90025
#   very_good       0.58      0.84      0.69    122896
#
# avg / total       0.60      0.60      0.56    244674

rf = RandomForestClassifier(n_jobs=-1, n_estimators=100, random_state=100)
rf.fit(X_train, y_train)

y_predict_rf = rf.predict(X_test)

print 'prediction result from random forest'
print confusion_matrix(y_test, y_predict_rf)
print classification_report(y_pred=pd.Series(y_predict_rf), y_true=pd.Series(y_test))
#              precision    recall  f1-score   support
#
# exceptional       0.27      0.11      0.15     31753
#        good       0.54      0.54      0.54     90025
#   very_good       0.58      0.67      0.62    122896
#
# avg / total       0.52      0.55      0.53    244674
