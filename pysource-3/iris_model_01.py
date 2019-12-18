#!/usr/bin/python

#############################################################
## module: iris_model_01.py
## description: single feature classifier separating setosas
## from versicolors and virginicas on the basis of petal
## lengths based on the materials from 
## Ch. 2, Richert & Coeho. “Building ML Systems with Py.”
##
## Bugs to vladimir dot kulyukin at usu dot edu
#############################################################
#from matplotlib import pyplot as plt
import numpy as np

## load the data with load_iris from sklearn
from sklearn.datasets import load_iris
data = load_iris()

# load_iris returns an object with several fields
data_items = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names
 
## Get an array of string flower names
flower_names = target_names[target]
## flower_names is as follows
'''
['setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa'
 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa'
 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa'
 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa'
 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa'
 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa' 'setosa'
 'setosa' 'setosa' 'versicolor' 'versicolor' 'versicolor' 'versicolor'
 'versicolor' 'versicolor' 'versicolor' 'versicolor' 'versicolor'
 'versicolor' 'versicolor' 'versicolor' 'versicolor' 'versicolor'
 'versicolor' 'versicolor' 'versicolor' 'versicolor' 'versicolor'
 'versicolor' 'versicolor' 'versicolor' 'versicolor' 'versicolor'
 'versicolor' 'versicolor' 'versicolor' 'versicolor' 'versicolor'
 'versicolor' 'versicolor' 'versicolor' 'versicolor' 'versicolor'
 'versicolor' 'versicolor' 'versicolor' 'versicolor' 'versicolor'
 'versicolor' 'versicolor' 'versicolor' 'versicolor' 'versicolor'
 'versicolor' 'versicolor' 'versicolor' 'versicolor' 'versicolor'
 'versicolor' 'virginica' 'virginica' 'virginica' 'virginica' 'virginica'
 'virginica' 'virginica' 'virginica' 'virginica' 'virginica' 'virginica'
 'virginica' 'virginica' 'virginica' 'virginica' 'virginica' 'virginica'
 'virginica' 'virginica' 'virginica' 'virginica' 'virginica' 'virginica'
 'virginica' 'virginica' 'virginica' 'virginica' 'virginica' 'virginica'
 'virginica' 'virginica' 'virginica' 'virginica' 'virginica' 'virginica'
 'virginica' 'virginica' 'virginica' 'virginica' 'virginica' 'virginica'
 'virginica' 'virginica' 'virginica' 'virginica' 'virginica' 'virginica'
 'virginica' 'virginica' 'virginica']
'''

# The petal length is the feature at position 2 of each
# data item
petal_lengths = data_items[:, 2]
## petal_lengths is the following array:
'''
[ 1.4  1.4  1.3  1.5  1.4  1.7  1.4  1.5  1.4  1.5  1.5  1.6  1.4  1.1  1.2
  1.5  1.3  1.4  1.7  1.5  1.7  1.5  1.   1.7  1.9  1.6  1.6  1.5  1.4  1.6
  1.6  1.5  1.5  1.4  1.5  1.2  1.3  1.5  1.3  1.5  1.3  1.3  1.3  1.6  1.9
  1.4  1.6  1.4  1.5  1.4  4.7  4.5  4.9  4.   4.6  4.5  4.7  3.3  4.6  3.9
  3.5  4.2  4.   4.7  3.6  4.4  4.5  4.1  4.5  3.9  4.8  4.   4.9  4.7  4.3
  4.4  4.8  5.   4.5  3.5  3.8  3.7  3.9  5.1  4.5  4.5  4.7  4.4  4.1  4.
  4.4  4.6  4.   3.3  4.2  4.2  4.2  4.3  3.   4.1  6.   5.1  5.9  5.6  5.8
  6.6  4.5  6.3  5.8  6.1  5.1  5.3  5.5  5.   5.1  5.3  5.5  6.7  6.9  5.
  5.7  4.9  6.7  4.9  5.7  6.   4.8  4.9  5.6  5.8  6.1  6.4  5.6  5.1  5.6
  6.1  5.6  5.5  4.8  5.4  5.6  5.1  5.1  5.9  5.7  5.2  5.   5.2  5.4  5.1]
'''

# Build a boolean index array for all items that are setosas.
is_setosa = (flower_names == 'setosa')
## the contents of is_setosa are as follows; note only the first
## 50 elements are True.
'''
[ True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True  True False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False]
'''
## a side note on how one may want to build boolean index arrays
## for versicolor and virgnicia
'''
>>> is_versicolor = (flower_names == 'versicolor')
>>> is_versicolor
array([False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False], dtype=bool)
>>> is_virginica = (flower_names == 'virginica')
>>> is_virginica
array([False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True], dtype=bool)
'''

# find and print out the maximum petal lengths for
# setosas and the minimum petal length values for non-setosas
max_setosa = petal_lengths[is_setosa].max()
min_non_setosa = petal_lengths[~is_setosa].min()
print("Maximum of setosa's petal lengths: {0}.".format(max_setosa))
print("Minimum of others's petal lengths: {0}.".format(min_non_setosa))

## petal length model to separate setosas from non-setosas.
def petal_length_model_for_setosa(petal_length_vals):
    classification_results = []
    for pl in petal_length_vals:
        if pl < 2:
            classification_results.append('setosa')
        else:
            classification_results.append('non-setosa')
    return classification_results

## here is how one can compute the accuracy of our model to
## separate setosas from versicolors and virginicas.
def compute_accuracy_of_petal_length_model_for_setosa(petal_length_vals):
    model_counts = petal_length_model_for_setosa(petal_length_vals).count('setosa')
    data_counts = flower_names.tolist().count('setosa')
    return model_counts/float(data_counts)
