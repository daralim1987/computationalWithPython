#!/usr/bin/python

################################
# Code fragments from Ch. 3, p. 53 in
# Building Machine Learning Systems with Python
# by Willi Richert and Luis Pedro Coelho
#
# bugs to vladimir dot kulyukin at usu dot edu
################################

import os
import sys
import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer
from utils import DATA_DIR

TOY_DIR = os.path.join(DATA_DIR, 'toy')
posts = [open(os.path.join(TOY_DIR, f)).read() for f in os.listdir(TOY_DIR)]

vectorizer_with_stop_words = CountVectorizer(min_df=1, stop_words='english')
feat_mat = vectorizer_with_stop_words.fit_transform(posts)
num_posts, num_feats = feat_mat.shape
print('features after stoplisting:')
print('#samples: %d, #features: %d' % (num_posts, num_feats))
print(vectorizer_with_stop_words.get_feature_names())


