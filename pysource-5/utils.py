#!/usr/bin/python

#################################################
# Code fragments from Ch. 3 in
# Building Machine Learning Systems with Python
# by Willi Richert and Luis Pedro Coelho
#
# bugs to vladimir dot kulyukin at usu dot edu
##################################################

import os
import sys
import scipy as sp

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')

if not os.path.exists(DATA_DIR):
    print('invalid directory')
    sys.exit(1)

CHART_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'charts')

if not os.path.exists(CHART_DIR):
    os.mkdir(CHART_DIR)

def euclid_dist(v1, v2):
    diff = v1 - v2
    return sp.linalg.norm(diff.toarray())

def norm_euclid_dist(v1, v2):
    v1_normalized = v1/sp.linalg.norm(v1.toarray())
    v2_normalized = v2/sp.linalg.norm(v2.toarray())
    diff = v1_normalized - v2_normalized
    return sp.linalg.norm(diff.toarray())

def display_feat_mat(feat_mat, num_docs):
    for i in range(0, num_docs):
        print('fv %d %s:' % (i, feat_mat.getrow(i).toarray()))

def find_closest_doc(vectorizer, user_query, docset,
                    doc_feat_mat, dist_fun, num_docs):
    # compute feature vector of user_query
    user_query_vec = vectorizer.transform([user_query])
    print('user query: %s' % user_query)
    print('user query vector: %s' % user_query_vec)
    best_doc = None
    best_dist = sys.maxint
    best_i = None # number of best doc match
    for i in xrange(0, num_docs):
        doc = docset[i]
        # skip the doc if it is equal to user_query
        if user_query == doc:
            continue
        # retrieve feature vector of a doc in doc feature matrix
        doc_vec = doc_feat_mat.getrow(i)
        # compute the distance b/w user_query_vector and document vector
        d = dist_fun(user_query_vec, doc_vec)
        print('=== Post %i with dist=%.2f: %s' % (i, d, doc))
        if d < best_dist:
            best_dist = d
            best_i = i
    print('Best post is %i with dist = %.2f' % (best_i, best_dist))

#print(DATA_DIR)
#print(CHART_DIR)

