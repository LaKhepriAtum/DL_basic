# -*- coding: utf-8 -*-
"""exam28_iris06_ADA_BOOST_Forest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gqDaH1LVdc2TWoP200WncXB0a66wbxke
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import *
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn import tree

plt.rcParams['figure.figsize'] = [7, 7]
sns.set(style='darkgrid')
plt.rcParams['scatter.edgecolors'] = 'black'
pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)
pd.set_option('display.unicode.east_asian_width', True)

iris_dataset = load_iris()
iris = pd.DataFrame(iris_dataset.data,
        columns=iris_dataset.feature_names)
labels = iris_dataset.target_names
iris.info()
print(iris.head())

label = iris_dataset.target
print(label)

scaler = StandardScaler()
iris = scaler.fit_transform(iris)
Features = pd.DataFrame(iris, columns=['SL', 'SW', 'PL', 'PW'])
print(Features.shape)

X_train, X_test, Y_train, Y_test = train_test_split(
            Features, label, test_size=0.2)

n_estimators = [50, 100, 150, 200, 250, 300, 350, 400] # 나무의 개수
learing_rate = [0.1, 0.2, .3 , .4, .5, .6, .7, .8, .9, 1.0] # 학습을 어떻게 할 것인지
algorithm = ['SAMME', 'SAMME.R'] # 수식이 조금 다르다
param = {'n_estimators': n_estimators, 'learning_rate': learing_rate, 'algorithm':algorithm}
cv = StratifiedShuffleSplit(n_splits=5, test_size = 0.2, random_state=868)
iris_AdaB = GridSearchCV(estimator = AdaBoostClassifier(), param_grid=param, scoring= 'accuracy',
                         n_jobs = -1, cv = cv) # for문 200번, n_jobs->cpu몇개 -1 =>전부
iris_AdaB.fit(X_train, Y_train)

print(iris_AdaB.best_score_)
print(iris_AdaB.best_params_)
print(iris_AdaB.best_estimator_) #SAMME.R이 디폴트 , 파라미터 값은 정해졌다.model = iris_AdaB.best_estimator_

for i in range(1, 100):
  X_train, X_test, Y_train, Y_test = train_test_split(
            Features, label, test_size=0.2, random_state= i)
  iris_AdaB = AdaBoostClassifier(learning_rate=0.7, n_estimators=400)
  iris_AdaB.fit(X_train, Y_train)

  train_score = iris_AdaB.score(X_train, Y_train)
  test_score = iris_AdaB.score(X_test, Y_test)
  if test_score >= train_score:
    print('test : {} train: {} random_state : {}'.format(test_score, train_score, i))

X_train, X_test, Y_train, Y_test = train_test_split(
          Features, label, test_size=0.2, random_state=42)
iris_AdaB = AdaBoostClassifier(learning_rate=0.7, n_estimators=400)
iris_AdaB.fit(X_train, Y_train)

train_score = iris_AdaB.score(X_train, Y_train)
test_score = iris_AdaB.score(X_test, Y_test)
if test_score >= train_score:
  print('test : {} train: {} '.format(test_score, train_score))

pd.DataFrame(confusion_matrix(Y_test, iris_AdaB.predict(X_test)),
        columns=['P_setosa', 'P_versicolor', 'P_virginica'],
        index=['A_setosa', 'A_versicolor', 'A_virginica'])

print(classification_report(Y_test, iris_AdaB.predict(X_test)))

