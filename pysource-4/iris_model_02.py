#!/usr/bin/python

################################################################
## module: iris_model_02.py
## description: single feature classifier separating virginicas
## from versicolors based on the materials from 
## Ch. 2, Richert & Coeho. "Building ML Systems with Py."
##
## Bugs to vladimir dot kulyukin at usu dot edu
################################################################

from matplotlib import pyplot as plt
import numpy as np

# load the data with load_iris from sklearn
from sklearn.datasets import load_iris
data = load_iris()

# load_iris returns an object with several fields
flower_items = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names
 
## Get an array of string flower names
flower_names = target_names[target]

# The petal length is the feature at column 2
petal_lengths = flower_items[:, 2]

# Build an array of booleans:
is_setosa = (flower_names == 'setosa')

# we find and print out the maximum petal lengths for
# setosas and the minimum petal length values for non-setosas
max_setosa = petal_lengths[is_setosa].max()
min_non_setosa = petal_lengths[~is_setosa].min()

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
def compute__accuracy_of_petal_length_model_for_setosa(petal_length_vals):
    model_counts = petal_length_model_for_setosa(petal_length_vals).count('setosa')
    data_counts = flower_names.tolist().count('setosa')
    return model_counts/float(data_counts)

## flower_fvs - flower feature vectors
def compute_best_threshold_model_for_virginica(flower_fvs, labels):
    best_fn = 0
    best_th = 0
    best_reverse = False
    best_acc = 0
    # ~ is the boolean negation operator
    # non_setosas are the virginica and versicolor feature vectors
    non_setosas = flower_fvs[~is_setosa]
    # labels are strings that are not Iris Setosa
    non_setosa_names = labels[~is_setosa]
    # is_virginica is an array of booleans
    is_virginica = (non_setosa_names == 'virginica')
    # Initialize best_acc to an impossibly low value
    best_acc = -1.0
    # features.shape returns (num_rows, num_cols)
    # features.shape[1] returns num_cols
    # for each possible feature, i.e., num_cols
    # this is where we can begin to iterate through each possible
    # feature number (fn)
    for fn in xrange(non_setosas.shape[1]):
        # inside the loop we are going to test all possible thresholds:
        # the thresh is an array of all possible values of
        # the features.
        # obtain all possible values for the selected feature fn
        possible_thresholds = non_setosas[:,fn]
        # for each possible threshold in possible_thresholds
        for pt in possible_thresholds:
            # get the array of values of that feature
            feature_vals = non_setosas[:, fn]
            # get a boolean array of when the value of that feature is
            # greater than a threshold
            predictions = (feature_vals > pt)
            # acc is the sum of 1's (Trues) divided by the length of predictions
            acc = (predictions == is_virginica).mean()
            # compute reverse accuracy: the accuracy of detecting non-virginicas
            rev_acc = (predictions == ~is_virginica).mean()
            if rev_acc > acc:
                reverse = True
                acc = rev_acc
            else:
                reverse = False

            if acc > best_acc:
                best_acc = acc
                best_fn = fn
                best_th = pt
                best_reverse = reverse
    #print(best_fn, best_th, best_reverse, best_acc)
    return (best_fn, best_th, best_reverse, best_acc)

petal_widths = flower_items[:, 3]
def petal_width_model_for_virginica(petal_width_vals):
    classification_results = []
    for pw in petal_width_vals:
        if pw > 1.6:
            classification_results.append('virginica')
        else:
            classification_results.append('non-virginica')
    return classification_results

## here is how one can compute the accuracy of our model to
## separate setosas from versicolors and virginicas.
def compute_accuracy_of_petal_width_model_for_virginica(petal_width_vals):
    model_counts = petal_width_model_for_virginica(petal_width_vals).count('virginica')
    data_counts = flower_names.tolist().count('virginica')
    return model_counts/float(data_counts)

## non_setosa_petal_widths = petal_widths[~is_setosa]
if __name__ == '__main__':
    print('Maximum of setosa petal lengths: {0}.'.format(max_setosa))
    print('Minimum of other  petal lengths: {0}.'.format(min_non_setosa))
    print compute_best_threshold_model_for_virginica(flower_items, flower_names)
