#!/usr/bin/python

##############################################################
# module: find_post_with_kmeans.py
# description: finding related posts with k-means;
# based on code fragments from Ch 3, Section 'Clustering' 
# that in 'Building Machine Learning Systems with Python'
# by Richert and Coelho.
#
# bugs to vladimir dot kulyukin at usu dot edu
###############################################################

import os
import sys
import sklearn.datasets
import scipy as sp

## 1. choose 6 training groups
groups = ['comp.graphics', 'comp.os.ms-windows.misc',
          'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware',
          'comp.windows.x', 'sci.space']

## 2. create train data
train_data = sklearn.datasets.fetch_20newsgroups(subset='train',
                                                 categories=groups)
## 3. this prints ('Number of training posts in tech groups:', 3529)
print('Number of training posts in tech groups:', len(train_data.filenames))

## 4. get the labels of train_data.target
labels = train_data.target
num_clusters = 50  # sp.unique(labels).shape[0]

#print(labels)

## ============ This is where K-Means begins ================
## this is the number of clusters needed by k-means. we
## can experiment with different numbers of clusters
num_clusters = 50  # sp.unique(labels).shape[0]

import nltk.stem
english_stemmer = nltk.stem.SnowballStemmer('english')

from sklearn.feature_extraction.text import TfidfVectorizer

class StemmedTfidfVectorizer(TfidfVectorizer):

    def build_analyzer(self):
        analyzer = super(TfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = StemmedTfidfVectorizer(min_df=10,
                                    stop_words='english',
                                    decode_error='ignore')

## build feature matrix from train_data
train_data_feat_mat = vectorizer.fit_transform(train_data.data)
num_samples, num_features = train_data_feat_mat.shape
print('#samples: %d, #features: %d' % (num_samples, num_features))
# samples: 3529, #features: 4712

from sklearn.cluster import KMeans

## create k-means clustering algorithm
km = KMeans(n_clusters=num_clusters, n_init=1, verbose=1, random_state=3)
## km and clustered data can be persisted
clustered_data = km.fit(train_data_feat_mat)

print('km.labels_=%s' % km.labels_)
# after the clustering is done, each data item
# has its own cluster label ranging from 0 to 49.
print('km.labels_=%s' % km.labels_)
print('len(km.labels_)=%d' % len(km.labels_))
# there are 3529 samples
# the number of samples is the same as the number of labels
# each label is an integer 0 <= i <= 49. or 0 <= i <= n-1
# where n is the number of clusters.
print('max label = %d' % max(km.labels_))
print('min label = %d' % min(km.labels_))

from sklearn import metrics
print('Homogeneity: %0.3f' % metrics.homogeneity_score(labels, km.labels_))
# Homogeneity: 0.400
print('Completeness: %0.3f' % metrics.completeness_score(labels, km.labels_))
# Completeness: 0.206
print('V-measure: %0.3f' % metrics.v_measure_score(labels, km.labels_))
# V-measure: 0.272
print('Adjusted Rand Index: %0.3f' %
      metrics.adjusted_rand_score(labels, km.labels_))
# Adjusted Rand Index: 0.064
print('Adjusted Mutual Information: %0.3f' %
      metrics.adjusted_mutual_info_score(labels, km.labels_))
# Adjusted Mutual Information: 0.197
print(('Silhouette Coefficient: %0.3f' %
       metrics.silhouette_score(train_data_feat_mat, labels, sample_size=1000)))
# Silhouette Coefficient: 0.006

new_post = \
    """Disk drive problems. Hi, I have a problem with my hard disk.
After 1 year it is working only sporadically now.
I tried to format it, but now it doesn't boot any more.
Any ideas? Thanks.
"""

new_post_vec = vectorizer.transform([new_post]).getrow(0).toarray()
km_predicted_labels = km.predict(new_post_vec)
print('len(km_predicted_labels)=%d' % len(km_predicted_labels))

## 1) predict the top cluster label for the new post
top_new_post_label = km.predict(new_post_vec)[0]

#print(top_new_post_label)

## here is an example of nozero() method.
## >>> np.array([True, False, True, False])
## array([ True, False,  True, False], dtype=bool)
##>>> np.array([True, False, True, False]).nonzero()
##(array([0, 2]),)
## >>> np.array([True, False, True, False]).nonzero()[0]
## array([0, 2])

## 2) find the labels of the posts in the same cluster.
posts_in_same_cluster = (km.labels_ == top_new_post_label).nonzero()[0]
## match the new post to the posts in the same cluster
## what is the reduction of the search space? let's find out:
## >>> len(train_data.filenames)
## 3529
## >>> len(posts_in_same_cluster)
## 122
## so, instead of matching aginst 3529 feature vectors, we are
## matching only against 122, i.e., about 3% of the available
## feature vectors.

## 3) go through the labels in the same cluster and
## save the distances.
similar_posts = []
for i in posts_in_same_cluster:
    dist = sp.linalg.norm(new_post_vec - train_data_feat_mat[i])
    similar_posts.append((dist, train_data.data[i]))

## similar_posts is a list of 2-tuples (dist, post_text).
## 4) sort the posts by their score from smallest to largest
similar_posts.sort(key=lambda post: post[0])

## similar_posts[0][0] to access the distance
## similar_posts[0][1] to access the post's text

