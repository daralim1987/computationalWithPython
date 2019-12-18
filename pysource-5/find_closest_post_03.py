#!/usr/bin/python

###########################################################
# module: find_closest_post_03.py
# description: CountVectorizer with stemming and
# stoplisting based on code fragments from Ch 3, p. 56 in
# Building Machine Learning Systems with Python
# by Willi Richert and Luis Pedro Coelho.
#
# Bugs to vladimir dot kulyukin at usu dot edu
############################################################

import os
import sys
import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer
from utils import DATA_DIR
from text_retrieval_utils import *

TOY_DIR = os.path.join(DATA_DIR, 'toy')
raw_posts = [open(os.path.join(TOY_DIR, f)).read() for f in os.listdir(TOY_DIR)]

## ========= Vectorizer with Stopwords & Stemming ===========
    
import nltk.stem
english_stemmer = nltk.stem.SnowballStemmer('english')
class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

stemmed_vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')
post_feat_mat_3= stemmed_vectorizer.fit_transform(raw_posts)
num_raw_posts_3, num_feats_3 = post_feat_mat_3.shape
print 'features after stemming'
print('#samples_3: %d, #features_2: %d' % (num_raw_posts_3, num_feats_3))
print(stemmed_vectorizer.get_feature_names())

def find_closest_post(new_raw_post, dist_fun):
    global stemmed_vectorizer
    global post_feat_mat_3
    global num_raw_posts_3
    global raw_posts
    find_closest_post_aux(stemmed_vectorizer, new_raw_post,  raw_posts,
                          post_feat_mat_3, dist_fun, num_raw_posts_3)
