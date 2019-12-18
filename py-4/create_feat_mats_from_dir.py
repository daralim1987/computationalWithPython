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

vectorizer = CountVectorizer(min_df=1)

feat_mat = vectorizer.fit_transform(posts)
num_samples, num_feats = feat_mat.shape
print('num samples: %d, num feats: %d' % (num_samples, num_feats))
print(vectorizer.get_feature_names())

'''
>>> new_post = 'imaging databases'
>>> new_post_vec = vectorizer.transform([new_post])
>>> new_post_vec
<1x25 sparse matrix of type '<type 'numpy.int64'>'
	with 2 stored elements in Compressed Sparse Row format>
>>> print new_post_vec
  (0, 5)	1
  (0, 7)	1
>>> print(new_post_vec.toarray())
[[0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]]
>>> len(new_post_vec.toarray()[0])
25
'''


