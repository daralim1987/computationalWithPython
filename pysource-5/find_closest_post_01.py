#!/usr/bin/python

##################################################
# module: find_closest_post_01.py
# description: vanilla vectorizer w/o
# stemming or stoplisting based on
# code fragments from Ch 3, p. 56 in
# Building Machine Learning Systems with Python
# by Willi Richert and Luis Pedro Coelho.
#
# Bugs to vladimir dot kulyukin at usu dot edu
###################################################

import os
import sys
import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer
from utils import DATA_DIR
from text_retrieval_utils import *

TOY_DIR = os.path.join(DATA_DIR, 'toy')
raw_posts = [open(os.path.join(TOY_DIR, f)).read()
             for f in os.listdir(TOY_DIR)]

##*********** Vanilla Vectorizer w/o Stemming or Stoplisting ***********
vectorizer = CountVectorizer(min_df=1)

## feature matrix
post_feat_mat = vectorizer.fit_transform(raw_posts)
## get the number of posts and features
num_raw_posts, num_raw_feats = post_feat_mat.shape
print('#samples: %d, #features: %d' % (num_raw_posts, num_raw_feats))
## display feature names
print(vectorizer.get_feature_names())

## vectorize a new post - 'imaging databases'.
# new_post = 'imaging databases'
# new_post_vec = vectorizer.transform([new_post])
# print(new_raw_post_vec)
# print('fv r %s' % new_post_vec.toarray())

def find_closest_post(new_raw_post, dist_fun):
    global vectorizer
    global post_feat_mat
    global num_raw_posts
    global raw_posts
    find_closest_post_aux(vectorizer, new_raw_post,  raw_posts,
                          post_feat_mat, dist_fun, num_raw_posts)
