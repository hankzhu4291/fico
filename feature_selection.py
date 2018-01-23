import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import tree


data_extracted = pd.read_csv('./data/data_extracted_feature.csv')

X = data_extracted.drop('fico', axis=1)
y = data_extracted['fico']

y_level = []
for i in y:
    if i >= 800:
        y_level.append('exceptional')
    elif i>=740:
        y_level.append('very_good')
    else:
        y_level.append('good')

y_credit_level = pd.Series(y_level)

features = list(X.columns)

# use decision tree to do feature selection
print 'use decision tree to do feature selection'
tr = tree.DecisionTreeClassifier(random_state=121)
tr.fit(X,y_credit_level)

feature_importance = pd.DataFrame({
    'feature': features,
    'importance': tr.feature_importances_
})

plt.figure(figsize=(20,10))
sns.barplot(x='feature', y='importance', data=feature_importance.sort_values(by='importance'))
plt.show()

# select features with importance over 0.0001
selected_features = X.iloc[:, tr.feature_importances_>0.0001]
fico = pd.DataFrame({'fico': y_credit_level})
data_selected_feature = pd.concat([selected_features, fico], axis=1)
data_selected_feature.to_csv('./data/data_selected_feature_class.csv', index=False)
