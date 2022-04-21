# -*- coding: utf-8 -*-
"""exam05_matpoltlib_visualization01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mCZZQG8yOAKdJl-g5WtuwwwGtTWZfN_C

#시각화
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 70

fig = plt.figure(figsize = (8,5)) #, dpi = 80 여기서 적을 수 있지만 매번하기 귀찮기 때문에 import에 미리 설정
ax = fig.add_axes([0,0,1,1]) # x좌표시작,y좌표시작,x축 사이즈,y사이즈 => 시작점의 좌표, 폭 , 높이
ax.set_title('figure')
plt.show()

"""##figure제작 -> add_axes"""

# figure 의 크기는 0~1
X = [0,1]
Y = [0,1]
fig = plt.figure(figsize = (8,5)) # figure를 제작
ax = [None, None, None]
ax[0] = fig.add_axes([0.1, 0.1, 0.4, 0.8]) # ax[0]는 
ax[1] = fig.add_axes([0.55, 0.15, 0.35, 0.4])
ax[2] = fig.add_axes([0.65, 0.6, 0.2, 0.3])
for i in range(3):
  ax[i].set_title('ax[{}]'.format(i))
  ax[i].set_xticks([]) #x축의 눈금 제거
  ax[i].set_yticks([]) #y축의 눈금 제거
ax[0].plot(X,Y) # [0]번째 인덱스에 넣기 
plt.show()

fig, ax = plt.subplots()
plt.show

"""##subplots 으로 figure, axes 한번에 제작"""

fig, axes = plt.subplots(2,3, figsize = (8,5)) # 2,3열, 사이즈 설정
axes[1,1].plot(X,Y)
plt.tight_layout() # 붙어있는 그래프 띄우기
plt.show()

"""## figure 제작 -> subplot2grid """

fig = plt.figure(figsize = (8,5)) # bpi의 8개, 5개
axes = []
axes.append(plt.subplot2grid((2,3),(0,0)))
axes.append(plt.subplot2grid((2,3),(0,1)))
axes.append(plt.subplot2grid((2,3),(0,2)))
axes.append(plt.subplot2grid((2,3),(1,0)))
axes.append(plt.subplot2grid((2,3),(1,1)))
axes.append(plt.subplot2grid((2,3),(1,2)))
# 이방법은 사이즈 조절이 안 된다.
plt.show()

fig = plt.figure(figsize = (8,5))
axes = []
axes.append(plt.subplot2grid((3,4), (0,0), colspan=2, rowspan = 2)) # 3행 4열, 0행0열에서 2개 쓴다 rowspan = 아래, colspan = 옆
axes.append(plt.subplot2grid((3,4), (0,2)))
axes.append(plt.subplot2grid((3,4), (0,3), rowspan = 3))
axes.append(plt.subplot2grid((3,4), (1,2)))
axes.append(plt.subplot2grid((3,4), (2,0), colspan = 3))
for i in range(5):
  axes[i].set_title('axes[{}]'.format(i))
  axes[i].set_xticks([])
  axes[i].set_yticks([])
fig.tight_layout(pad=2)
plt.show()

"""## figure 제작 -> add_subplot"""

fig = plt.figure(figsize  = (8,5))
gs = fig.add_gridspec(3,4) #3행 4열

axes = [None] * 5
axes[0] = fig.add_subplot(gs[0:2, 0:2])
axes[1] = fig.add_subplot(gs[0,2])
axes[2] = fig.add_subplot(gs[:,-1])
axes[3] = fig.add_subplot(gs[1,2])
axes[4] = fig.add_subplot(gs[2,0:3])
for i in range(5):
  axes[i].set_title('axes[{}]'.format(i))
  axes[i].set_xticks([])
  axes[i].set_yticks([])
fig.tight_layout(pad=2)
plt.show()

"""## 독특한 subplots"""

fig, axes = plt.subplots()
axin1 = axes.inset_axes([0.8, 0.1, 0.15, 0.15],  # 0.8, 0.1 에서 시작, 폭 0.15 높이 0.15
                        xticks = [], yticks = [])
plt.show()

from mpl_toolkits.axes_grid1 import axes_divider
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

fig, axes = plt.subplots()
ax_divider = make_axes_locatable(axes)
axes = ax_divider.append_axes("right", size='10%', pad='5%', xticks=[], yticks =[])
plt.show() # 오른쪽의 작은 것은 색상표 같은 경우에 많이 사용

