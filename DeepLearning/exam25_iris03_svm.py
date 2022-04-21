# -*- coding: utf-8 -*-
"""exam25_iris03_SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wUlhQzwnvMao6bmxgbfGxFM_V-LxR55G
"""

#SVM의 장점은 빠르다, SV만으로 초평면을 그리기 때문에
# cv = cross valudation 교차검증
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import *
from sklearn.metrics import classification_report, confusion_matrix

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

from sklearn import svm
from sklearn.model_selection import *
kernel_list = ['linear', 'poly', 'rbf', 'sigmoid']
params = dict(kernel = kernel_list)
cv = StratifiedShuffleSplit(n_splits = 5, test_size = 0.2, random_state=2985)
irisSVM = svm.SVC(C = 1.0, random_state= 2985, class_weight = 'balanced') # SVM으로 회기 분석도 가능(값 예측) ,C의 디폴트 ->1.0 마진을 허용=이상치에 관대(과적합 방지를 위해)
kernel_Type = GridSearchCV(irisSVM, params, cv = cv) # kernel을 ['linear', 'poly', 'rbf', 'sigmoid']로 하나하나 다 해본다
kernel_Type.fit(Features, label)
scores = kernel_Type.cv_results_['mean_test_score']

for score, kernel in zip(scores, kernel_list):
  print(f'{kernel} {score:f}')
# poly: n차식에 따라 변곡점의 개수가 달라진다-> 처음에는 디폴트만-> 차수에 따라 결과가 달라진다.초평면이 얼마나 울퉁불퉁한지는 차수에 따라 달라진다. 
# 디폴트는 rbf(차수가 무한대에 가까운 poly->거의 원)

degree_list  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
params = dict(degree = degree_list)
irisSVM = svm.SVC(C = 1.0, random_state=2985,
                  class_weight = 'balanced',kernel = 'poly' )
degree_Type = GridSearchCV(irisSVM, params, cv = cv)
degree_Type.fit(Features, label)
scores = degree_Type.cv_results_['mean_test_score']

for score, degree in zip(scores, degree_list):
  print(f'{degree} {score:f}')

kernel_list = ['linear', 'poly', 'rbf', 'sigmoid']
params = dict(kernel = kernel_list)
cv = StratifiedShuffleSplit(n_splits = 5, test_size = 0.2, random_state=2985)
irisSVM = svm.SVC(C = 1.0, random_state= 2985, class_weight = 'balanced', degree = 2) # SVM으로 회기 분석도 가능(값 예측). degree 로 poly의 차수 결정, 
kernel_Type = GridSearchCV(irisSVM, params, cv = cv) # kernel을 ['linear', 'poly', 'rbf', 'sigmoid']로 하나하나 다 해본다
kernel_Type.fit(Features, label)
scores = kernel_Type.cv_results_['mean_test_score']

for score, kernel in zip(scores, kernel_list):
  print(f'{kernel} {score:f}')

np.geomspace(1,1000, num= 4) # 로그 스케일의 등간격으로 나눠준다

X_train, X_test, Y_train, Y_test = train_test_split(
    Features, label, test_size=0.2)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

C_list = np.geomspace(10000, 0.0001, num = 50)
print(C_list)

params = dict(C=C_list)
cv = StratifiedShuffleSplit(n_splits = 5, test_size = 0.2, random_state=2958) # StratifiedShuffleSplit-> 5개로 나누고, test은20%
iris_SVM = svm.SVC(random_state=2958, class_weight = 'balanced',
                   kernel = 'poly', degree = 1) # SVM객체를 만드는 것
C_Type = GridSearchCV(iris_SVM, params, cv = cv) # 교차 검증할 때 cv = StratifiedShuffleSplit(n_splits = 5, test_size = 0.2, random_state=2958) 이용, GridSearchCV-> 알아서 for문
C_Type.fit(X_train, Y_train) # 데이터를 cv 형태로, accuracy를 주는 단계
scores = C_Type.cv_results_['mean_test_score'] #test_size = 0.2 를 가지고 정확도를 구한다

for score, C in zip(scores, C_list):
  print(f'{C: .3f} {score: .3f}')

#GridSearchCV 을 한 것
for c in C_list:
    model1 = svm.SVC(C=c, kernel='poly', class_weight='balanced',
                     gamma='scale', degree=1)
    model1.fit(X_train, Y_train)
    train_score = model1.score(X_train, Y_train)
    test_score = model1.score(X_test, Y_test)
    print('The Accuracy @ {} C parameter, Train score is {}, Test score is {}'.format(c, train_score, test_score))

accuracies = cross_val_score(svm.SVC(kernel = 'poly', degree = 1,C=75.43), # 최적화된 모델의 값들
                             Features, label, cv = cv)# C 마진을 얼마나 크게 잡을 것인가=오차를 얼마나 적용할 것인가(너무 적으면 과적합, 너무 크면 과소적합 ) 
                                     # 적당한 값을 찾아야 한다-> 다 돌려보고 가장 좋은 것을 찾는다
print('Cross-Validation accuracy scores: {}'.format(accuracies)) #cv가 5개씩 나누게 되어있다
print('Mean Cross-Validation accuracy score: {}'.format(round(accuracies.mean(), 5)))

for i in range(1, 1000):
  X_train, X_test, Y_train, Y_test = train_test_split(
      Features, label, test_size = 0.2, random_state = i)
  iris_SVM = svm.SVC(kernel = 'poly', degree = 1,C=75.43, # 최적화된 모델의 값들
                             class_weight= 'balanced')
  iris_SVM.fit(X_train, Y_train)
  train_score = iris_SVM.score(X_train, Y_train)
  test_score = iris_SVM.score(X_test, Y_test)
  if test_score>= train_score:
    print('Test : {} Train : {} RandomState : {}'.format(test_score, train_score, i))

X_train, X_test, Y_train, Y_test = train_test_split(
        Features, label, test_size=0.2, random_state=332)
iris_SVM = svm.SVC(kernel='poly', degree=1,
            C=75.43, class_weight='balanced')
iris_SVM.fit(X_train, Y_train)
train_score = iris_SVM.score(X_train, Y_train)
print(train_score)
test_score = iris_SVM.score(X_test, Y_test)
print(test_score)

pd.DataFrame(confusion_matrix(Y_test, iris_SVM.predict(X_test)),
                columns=['P_setosa', 'P_versicolor', 'P_virginica'],
                index=['A_setosa', 'A_versicolor', 'A_virginica'])

print(classification_report(Y_test, iris_SVM.predict(X_test)))
