#!/usr/bin/python

##########################################################
## Programmatic investigation of the features
## of the sklearn iris dataset covered in
## Ch. 2, Richert & Coeho. “Building ML Systems with Py.”
##
## Bugs to vladimir dot kulyukin at usu dot edu
##########################################################

import sys
import numpy as np
## the iris dataset is loaded with load_iris from sklearn
from sklearn.datasets import load_iris

## load_iris returns an object with several standard fields:
## data.feature_names
## data.data
## data.target
## data.target_names
iris_data = load_iris()

## ======== DATA.FEATURE_NAMES =======
## Sample run:
## > python investigate_iris_dataset.py feature_names
## <type 'list'>
## 4
## feature names:
## ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
##
## In other words, these are feature numbers and their names
## 0 - sepal length (cm)
## 1 - sepal width  (cm)
## 2 - petal length (cm)
## 3 - petal width  (cm)
def print_feature_names(data):
    feature_names = data.feature_names
    print type(feature_names)
    print len(feature_names)
    print 'feature names:'
    print feature_names

## ======== DATA.DATA =======
## Sample run of print_data_items
## > python investigate_iris_dataset.py data_items
## <type 'numpy.ndarray'>
## (150, 4)
## data items:
## [[ 5.1  3.5  1.4  0.2]
##  [ 4.9  3.   1.4  0.2]
##  [ 4.7  3.2  1.3  0.2]
##  [ 4.6  3.1  1.5  0.2]
##  [ 5.   3.6  1.4  0.2]
##  ...
##  [ 5.9  3.   5.1  1.8]]
def print_data_items(data):
    data_items = data.data
    print type(data_items)
    print data_items.shape
    print 'data items:'
    print data_items

## ======== DATA.TARGET =======
## Sample run of print_data_target
##> python investigate_iris_dataset.py target
##<type 'numpy.ndarray'>
##(150,)
##[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
## 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
## 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
## 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
## 2 2]
def print_data_target(data):
    target = data.target
    print type(target)
    print target.shape
    print target

## ======== DATA.TARGET_NAMES =======
## Sample run of print_target_names
## >python investigate_iris_dataset.py target_names
## <type 'numpy.ndarray'>
## (3,)
## ['setosa' 'versicolor' 'virginica']
def print_target_names(data):
    target_names = data.target_names
    print type(target_names)
    print target_names.shape
    print target_names

## Sample run if you want to retrieve all setosa items
## $ python investigate_iris_dataset.py setosa
## (50, 4)
## All data items classified as setosa
## [[ 5.1  3.5  1.4  0.2]
##  [ 4.9  3.   1.4  0.2]
##  ...
##  [ 5.   3.3  1.4  0.2]]
##
##  Sample run if you want to retrieve all versicolor items
## $ python investigate_iris_dataset.py versicolor
## (50, 4)
## All data items classified as versicolor
## [[ 7.   3.2  4.7  1.4]
##  [6.4  3.2  4.5  1.5]
##  ...
##  [ 5.7  2.8  4.1  1.3]]
##
## $ python investigate_iris_dataset.py virginica
## (50, 4)
## All data items classified as virginica
## [[ 6.3  3.3  6.   2.5]
##  [ 5.8  2.7  5.1  1.9]
##  ...
##  [ 5.9  3.   5.1  1.8]]

## target_name == 'setosa', target_name == 'versicolor'
## target_name == 'virginica'.
def print_data_items_classified_as(data, target_name):
    target_names = data.target_names
    data_items = data.data
    target = data.target
    try:
        # find the index of target_name in list of target names
        t = target_names.tolist().index(target_name)
        ## get me all target items classified as t, where
        ## t is 0, 1, or 2: 0 for setosa, 1 for versicolor,
        ## 2 for virginica.
        target_items = data_items[target==t]
        print target_items.shape
        print 'All data items classified as', target_name
        print target_items
    except Exception as e:
        print e

## target numbers:
## 0 - setosa
## 1 - versicolor
## 2 - virginica
##
## feature numbers:
## 0 - sepal length (cm)
## 1 - sepal width  (cm)
## 2 - petal length (cm)
## 3 - petal width  (cm)
##
## If you want to get all sepal lengths of setosas:
## > get_all_feature_values_for_target(iris_data, 0, 0).
## [ 5.1  4.9  4.7  4.6  5.   5.4  4.6  5.   4.4  4.9  5.4  4.8  4.8  4.3  5.8
## 5.7  5.4  5.1  5.7  5.1  5.4  5.1  4.6  5.1  4.8  5.   5.   5.2  5.2  4.7
## 4.8  5.4  5.2  5.5  4.9  5.   5.5  4.9  4.4  5.1  5.   4.5  4.4  5.   5.1
## 4.8  5.1  4.6  5.3  5. ]
##
## if you want to get all sepal widths of setosas:
## > get_all_feature_values_for_target(iris_data, 0, 1)
## [ 3.5  3.   3.2  3.1  3.6  3.9  3.4  3.4  2.9  3.1  3.7  3.4  3.   3.   4.
## 4.4  3.9  3.5  3.8  3.8  3.4  3.7  3.6  3.3  3.4  3.   3.4  3.5  3.4  3.2
## 3.1  3.4  4.1  4.2  3.1  3.2  3.5  3.1  3.   3.4  3.5  2.3  3.2  3.5  3.8
## 3.   3.8  3.2  3.7  3.3]
##
## if you want to get all petal lengths of setosas:
##> get_all_feature_values_for_target(iris_data, 0, 2)
##[ 1.4  1.4  1.3  1.5  1.4  1.7  1.4  1.5  1.4  1.5  1.5  1.6  1.4  1.1  1.2
##  1.5  1.3  1.4  1.7  1.5  1.7  1.5  1.   1.7  1.9  1.6  1.6  1.5  1.4  1.6
##  1.6  1.5  1.5  1.4  1.5  1.2  1.3  1.5  1.3  1.5  1.3  1.3  1.3  1.6  1.9
##  1.4  1.6  1.4  1.5  1.4]
##
## if you want to get all petal widths of setosas:
## > get_all_feature_values_for_target(iris_data, 0, 3)
##[ 0.2  0.2  0.2  0.2  0.2  0.4  0.3  0.2  0.2  0.1  0.2  0.2  0.1  0.1  0.2
##  0.4  0.4  0.3  0.3  0.3  0.2  0.4  0.2  0.5  0.2  0.2  0.4  0.2  0.2  0.2
##  0.2  0.4  0.1  0.2  0.1  0.2  0.2  0.1  0.2  0.2  0.3  0.3  0.2  0.6  0.4
##  0.3  0.2  0.2  0.2  0.2]
##
## if you want to get all petal lengths of versicolor
## > get_all_feature_values_for_target(iris_data, 1, 2)
##[ 4.7  4.5  4.9  4.   4.6  4.5  4.7  3.3  4.6  3.9  3.5  4.2  4.   4.7  3.6
##  4.4  4.5  4.1  4.5  3.9  4.8  4.   4.9  4.7  4.3  4.4  4.8  5.   4.5  3.5
##  3.8  3.7  3.9  5.1  4.5  4.5  4.7  4.4  4.1  4.   4.4  4.6  4.   3.3  4.2
##  4.2  4.2  4.3  3.   4.1]
def get_all_feature_values_for_target(data, tn, fn):
    data_items = data.data
    target = data.target
    feature_vals = data_items[target==tn,fn]
    print feature_vals

## comment out when inside IDLE
'''
if __name__ == '__main__':
    if sys.argv[1] == 'feature_names':
        print_feature_names(iris_data)
    elif sys.argv[1] == 'data_items':
        print_data_items(iris_data)
    elif sys.argv[1] == 'target':
        print_data_target(iris_data)
    elif sys.argv[1] == 'target_names':
        print_target_names(iris_data)
    elif sys.argv[1] == 'setosa':
        print_data_items_classified_as(iris_data, 'setosa')
    elif sys.argv[1] == 'versicolor':
        print_data_items_classified_as(iris_data, 'versicolor')
    elif sys.argv[1] == 'virginica':
        print_data_items_classified_as(iris_data, 'virginica')
    else:
        get_all_feature_values_for_target(iris_data, 0, 0)
        print('unknown option')
'''
