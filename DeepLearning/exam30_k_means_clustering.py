# -*- coding: utf-8 -*-
"""exam30_k_means_clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hjjAUpTIN9SDs9zDPw3YpBcrsorQu5Au
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans

data = pd.read_csv('./datasets/wholesale.csv')
print(data.head())

scaled_data = normalize(data) #np.array로 바뀐다
scaled_data = pd.DataFrame(scaled_data, columns= data.columns)
print(scaled_data.head())

plt.figure(figsize=(5, 4))
plt.title('Dendrograms') # data 들이 얼마나 이질적인가를 나타내는 것
shc.dendrogram(shc.linkage(scaled_data, method='ward'))
plt.axhline(y=4, color='r', linestyle='--') # 수평선 그리기
plt.show()
# 이질적인 data를 2로 나누고 길이가 길수록 크게 이질적이다-> 얼마나 많이 떨어져 있는가

cluster = KMeans(n_clusters=3)
print(cluster.fit_predict(scaled_data))

plt.figure(figsize = (5,4))
plt.scatter(scaled_data['Milk'],
            scaled_data['Grocery'],
            c = cluster.labels_)
plt.show()

pd.plotting.scatter_matrix(scaled_data, figsize=(15, 15),
                           c=cluster.labels_)
plt.show()
