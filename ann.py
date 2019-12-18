#!/usr/bin/python

#####################################
# module: ann.py
# author: vladimir kulyukin
# description: 2 simple ANNs
#####################################

import numpy as np

## ================ DATA ===================

X = np.array([[0, 0],
              [1, 0],
              [0, 1],
              [1, 1]])

y_and = np.array([[0],
                  [0],
                  [0],
                  [1]])

y_or = np.array([[0],
                 [1],
                 [1],
                 [1]])

X1 = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 1]])

y1 = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 1]])

## ============== Designing and Training ==============

def sigmoid(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
        #return np.exp(-x)/((1 + np.exp(-x))**2)
    return 1 / (1 + np.exp(-x))

def build_2_3_1_nn():
    np.random.seed(1)
    W1 = np.random.randn(2, 3)
    W2 = np.random.randn(3, 1)
    return W1, W2
    
def build_8_3_8_nn():
    np.random.seed(1)
    W1 = np.random.randn(8, 3)
    W2 = np.random.randn(3, 8)
    return W1, W2

def train_3_layer_nn(numIters, X, y, build):
    W1, W2 = build()
    for j in range(numIters):
        Z2 = np.dot(X, W1)
        a2 = sigmoid(Z2)

        Z3 = np.dot(a2, W2)
        yHat = sigmoid(Z3)

        yHat_error = y - yHat
        yHat_delta = yHat_error * sigmoid(yHat, deriv=True)

        a2_error = yHat_delta.dot(W2.T)
        a2_delta = a2_error * sigmoid(a2, deriv=True)

        W2 += a2.T.dot(yHat_delta)
        W1 += X.T.dot(a2_delta)
    
    return W1, W2

## ============== Fitting ANN ==============

def fit_3_layer_nn(input0, W1, W2, thresh=0.4, thresh_flag=True):
    input1 = sigmoid(np.dot(input0, W1))
    output = sigmoid(np.dot(input1, W2))
    if thresh_flag == True:
        for x in np.nditer(output, op_flags=['readwrite']):
            if x > thresh:
                x[...] = 1
            else:
                x[...] = 0
        return output.astype(int)
    else:
        return output

