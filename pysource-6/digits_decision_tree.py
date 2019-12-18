#!/usr/bin/python

############################################################
# module: iris_decision_tree.py
# description: A decision tree for DIGITS datasets
#
# If you get "ImportError: No module named model_selection"
# when you run this module, run the following command:
#
# sudo pip install -U scikit-learn
#
# this pip install upgrades scikit-learn to version
# 0.18 where model_selection was added.
#
# bugs to vladimir dot kulyukin at usu dot edu
#############################################################

from sklearn.datasets import load_digits
from sklearn import tree, metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
import matplotlib.pyplot as plt
import numpy as np
from random import randint

digits_data = load_digits()
data_items = digits_data.data
target = digits_data.target
clf = tree.DecisionTreeClassifier(random_state=0)
dtr = clf.fit(data_items, target)
#print(dtr.predict(data_items))
#tree.export_graphviz(dtr, out_file='digits_tree.dot')

def run_train_test_split(classifier, n, test_size):
    for i in xrange(n):
        train_data, test_data, train_target, test_target = \
                    train_test_split(data_items, target,
                                     test_size=test_size, random_state=randint(0, 1000))
        test_len = float(len(test_target))
        dt = classifier.fit(train_data, train_target)
        acc_preds = sum(dt.predict(test_data)==test_target)
        print('train/test run %d: accuracy = %f' % (i, acc_preds/test_len))
        print('------------------------------------------')

def run_cross_validation(dtr, n):
    for i in xrange(n):
        ## cv specifies the number of folds data is split
        ## on of the folds is used for testing the remaining ones
        ## are used for training
        print('cross-validation run %d' % i)
        for cv in xrange(5, 16):
            cross_val = cross_val_predict(dtr, data_items, target, cv=cv)
            acc = sum(cross_val==target)/float(len(target))
            print('num_folders %d, accuracy = %f' % (cv, acc))
            print('------------------------------------------')

from sklearn.metrics import confusion_matrix
from matplotlib import pylab

plot_targets = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
plot_title = 'DIGITS Confusion Matrix'
def compute_train_test_confusion_matrix(clf, test_size):
    global data_items
    global target
    train_data, test_data, train_target, test_target = \
                    train_test_split(data_items, target,
                                     test_size=test_size, random_state=randint(0, 1000))
    dtr = clf.fit(train_data, train_target)
    clf_expected = test_target
    clf_predicted = dtr.predict(test_data)
    cm = confusion_matrix(clf_expected, clf_predicted)
    plot_confusion_matrix(cm, plot_targets, plot_title)
    print("Classification report for decision tree %s:\n%s\n"
          % (dtr, metrics.classification_report(clf_expected, clf_predicted)))
    print("Confusion matrix:\n%s" % cm)

def plot_confusion_matrix(cm, target_name_list, title):
    pylab.clf()
    pylab.matshow(cm, fignum=False, cmap='Blues', vmin=0, vmax=1.0)
    ax = pylab.axes()
    ax.set_xticks(range(len(target_name_list)))
    ax.set_xticklabels(target_name_list)
    ax.xaxis.set_ticks_position('bottom')
    ax.set_yticks(range(len(target_name_list)))
    ax.set_yticklabels(target_name_list)
    pylab.title(title)
    pylab.colorbar()
    pylab.grid(False)
    pylab.xlabel('Predicted class')
    pylab.ylabel('True class')
    pylab.grid(False)
    pylab.show()

if __name__ == '__main__':
    compute_train_test_confusion_matrix(clf, 0.3)
