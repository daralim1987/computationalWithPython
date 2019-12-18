#!/usr/bin/python

##########################################################
# module: text_retrieval_utils.py
# description: utilities used in find_closest_post_01.py,
# find_closes_post_02.py, and find_closest_post_03.py
# bugs to vladimir dot kulyukin at usu dot edu
##########################################################

import sys
import scipy.linalg
import numpy as np

## euclidiean dist
def dist_raw(v1, v2):
    delta = v1 - v2
    return scipy.linalg.norm(delta)

## normalized euclidiean distance
def dist_raw_norm(v1, v2):
    v1_normalized = v1/scipy.linalg.norm(v1)
    v2_normalized = v2/scipy.linalg.norm(v2)
    delta = v1_normalized - v2_normalized
    return scipy.linalg.norm(delta)

## Comment added in response to Evan Peterson's questions after my
## lecture on April 6, 2017.
## Note the difference b/w regular and normalized euclidean
## distances:
## >>> dist_raw_norm(np.array([1, 0, 1, 0]), np.array([5, 0, 5, 0]))
## 0.0
## >>> dist_raw(np.array([1, 0, 1, 0]), np.array([5, 0, 5, 0]))
## 5.6568542494923806

## debugging util
def display_feat_mat(feat_mat, num_posts):
    for i in range(0, num_posts):
        print("fv %d %s:" % (i, feat_mat.getrow(i).toarray()))

## the work horse that actually finds the closes post
## v is a vectorizer object.
def find_closest_post_aux(v, new_raw_post, raw_posts,
                    post_feat_mat, dist_fun, num_posts):
    # compute feature vector of new_raw_post
    # print 'new_raw_post:', new_raw_post
    new_post_vec = v.transform([new_raw_post]).getrow(0).toarray()
    assert new_post_vec is not None
    best_post = None
    best_dist = sys.maxint
    best_i = None # number of best post match
    # print('new_post_vec: %s' % str(new_post_vec))
    for i in xrange(0, num_posts):
        raw_post = raw_posts[i]
        # skip the post itself
        if raw_post == new_raw_post:
            continue
        # retrieve feature vector of a post in post feature matrix
        post_vec = post_feat_mat.getrow(i).toarray()
        print('new_post_vec: %s' % str(new_post_vec))
        print('post_vec:         %s' % str(post_vec))
        # compute the distance b/w post fv and new post fv
        d = dist_fun(new_post_vec, post_vec)
        print '=== Post %i with dist=%.2f: %s' % (i, d, raw_post)
        if d < best_dist:
            best_dist = d
            best_i = i
    print('Best post is %i with dist = %.2f' % (best_i, best_dist))

def unit_test_01():
    v1 = np.array([1, 2])
    v2 = np.array([2, 3])
    print dist_raw(v1, v2)


