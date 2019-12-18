#!/usr/bin/python

##########################################################
# module: train_test.py
# description: splitting data into training and testing
# sets and computing the goodness of fit with R^2.
##########################################################

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

pageRenderTime = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 10.0, 100)

fig1 = plt.figure(1)
fig1.suptitle('Page Render Time vs. Purchase Amount')
plt.xlabel('Page Render Time')
plt.ylabel('Purcahse Amount')
plt.grid()
plt.scatter(pageRenderTime, purchaseAmount)

## 80/20 split
trainPageTime = pageRenderTime[:80]
testPageTime = pageRenderTime[80:]

## 80/20 split on purchase amount
trainPurchaseAmount = purchaseAmount[:80]
testPurchaseAmount = purchaseAmount[80:]

fig2 = plt.figure(2)
fig2.suptitle('Train Page Time vs. Train Purchase Amount')
plt.xlabel('Train Page Render Time')
plt.ylabel('Train Purcahse Amount')
plt.grid()
plt.scatter(trainPageTime, trainPurchaseAmount)

trainX = np.array(trainPageTime)
trainY = np.array(trainPurchaseAmount)
polyfit = np.poly1d(np.polyfit(trainX, trainY, 8))
t = np.linspace(0, 7, 100)

fig3 = plt.figure(3)
fig3.suptitle('Polyfit over Training Data')
axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 100])
plt.scatter(trainX, trainY)
plt.plot(t, polyfit(t), c='r')

testX = np.array(testPageTime)
testY = np.array(testPurchaseAmount)
fig4 = plt.figure(4)
fig4.suptitle('Polyfit over Test Data')
axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 100])
plt.scatter(testX, testY)
plt.plot(t, polyfit(t), c='b')

## http://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html
from sklearn.metrics import r2_score
test_r2 = r2_score(testY, polyfit(testX))
print('Test R2  = %f' % test_r2)

train_r2 = r2_score(trainY, polyfit(trainX))
print('Train R2 = %f' % train_r2)

plt.show()
