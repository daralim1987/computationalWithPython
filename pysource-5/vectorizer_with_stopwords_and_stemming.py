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
import nltk.stem

TOY_DIR = os.path.join(DATA_DIR, 'toy')
posts = [open(os.path.join(TOY_DIR, f)).read() for f in os.listdir(TOY_DIR)]

english_stemmer = nltk.stem.SnowballStemmer('english')
class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

stemmed_vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')
feat_mat= stemmed_vectorizer.fit_transform(posts)
num_posts, num_feats = feat_mat.shape
print('features after stemming and stoplisting')
print('#samples_3: %d, #features_2: %d' % (num_posts, num_feats))
print(stemmed_vectorizer.get_feature_names())
