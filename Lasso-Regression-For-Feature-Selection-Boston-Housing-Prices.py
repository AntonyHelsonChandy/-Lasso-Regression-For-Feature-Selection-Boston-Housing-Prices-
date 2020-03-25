from sklearn.datasets import load_boston
import pandas as pd

bostona = load_boston()
bostona.keys()
boston_pd = pd.DataFrame(bostona.data)
boston_pd.columns = bostona.feature_names
boston_pd.head()
print(boston_pd.head())

#the output/ MEDV
boston_y = pd.DataFrame(bostona.target, columns = ['MEDV']) 
boston_y
print(boston_y.head())

import seaborn as sns

g = sns.pairplot(boston_pd)

from sklearn import linear_model

clf = linear_model.Lasso(alpha=0.1)
clf.fit(boston_pd,boston_y)
clf.coef_
print(clf.coef_)

import matplotlib.pyplot as plt

_=plt.plot(range(len(bostona.feature_names)),clf.coef_)
_=plt.xticks(range(len(bostona.feature_names)),bostona.feature_names,rotation=60)
_=plt.ylabel("Coefficients")
plt.show()


