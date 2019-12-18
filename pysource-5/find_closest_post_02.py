#!/usr/bin/python

##################################################
# module: find_closest_post_02.py
# description: CountVectorizer with stoplisting;
# based on code fragments from Ch 3, p. 56 in
# Building Machine Learning Systems with Python
# by Willi Richert and Luis Pedro Coelho.
#
# Bugs to vladimir dot kulyukin at usu dot edu
##################################################

import os
import sys
import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer
from utils import DATA_DIR
from text_retrieval_utils import *

TOY_DIR = os.path.join(DATA_DIR, 'toy')
raw_posts = [open(os.path.join(TOY_DIR, f)).read()
             for f in os.listdir(TOY_DIR)]

## =============== Vectorizer with Stopwords ==============
    
vectorizer_with_stop_words = CountVectorizer(min_df=1, stop_words='english')
post_feat_mat_2 = vectorizer_with_stop_words.fit_transform(raw_posts)
num_raw_posts_2, num_feats_2 = post_feat_mat_2.shape
print('features after stoplisting:')
print('#samples: %d, #features: %d' % (num_raw_posts_2, num_feats_2))
print(vectorizer_with_stop_words.get_feature_names())

def find_closest_post(new_raw_post, dist_fun):
    global vectorizer_with_stop_words
    global post_feat_mat_2
    global num_raw_posts_2
    global raw_posts
    find_closest_post_aux(vectorizer_with_stop_words, new_raw_post,  raw_posts,
                          post_feat_mat_2, dist_fun, num_raw_posts_2)



