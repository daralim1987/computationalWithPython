#!/usr/bin/python

############################################################
# module: svm_digits.py
# description: confusion matrices for 3
# different SVM classifiers on digits dataset
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

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets, metrics
from sklearn.model_selection import train_test_split
import random

## get the data, the data items, and target
iris_data = datasets.load_iris()
data_items = iris_data.data
data_target = iris_data.target

## let's create 3 classifiers
C = 1.0  # SVM regularization error parameter
# an svm classifier with linear kernel
lin_svc = svm.SVC(kernel='linear', C=C)
# an svm classifier with rbf kernel
rbf_svc = svm.SVC(kernel='rbf', C=C)
# an svm classifier with 3rd degree poly kernel
poly_svc = svm.SVC(kernel='poly', degree=3, C=C)

def print_svc_report(clf, data_items, data_target, test_size=0.3):
    #1. get train & test data and train and test targets
    train_data, test_data, train_target, test_target = \
                    train_test_split(data_items,
                                     data_target,
                                     test_size=test_size,
                                     random_state=random.randint(0, 1000))
    # 2. fit the classifier over the train data and train target
    clf.fit(train_data, train_target)
    # 3. set the ground true to test target vector
    clf_expected = test_target
    # 4. test the classifier on test data
    clf_predicted = clf.predict(test_data)
    # 5. print the classification report followed by confustion matrix
    print("Classification report for SVC with linear kernel %s:\n%s\n"
          % (clf, metrics.classification_report(clf_expected, clf_predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(clf_expected, clf_predicted))
    print('--------------------------------------------------')

## print three classification reports
if __name__ == '__main__':
    print_svc_report(lin_svc, data_items, data_target)
    print_svc_report(rbf_svc, data_items, data_target)
    print_svc_report(poly_svc, data_items, data_target)



