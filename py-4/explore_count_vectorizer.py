#!/usr/bin/python

####################################
# Code fragments from Ch. 3, p. 52 in "Building
# ML Systems with Python" by W. Richert & L. P. Coelho
#
# bugs to vladimir dot kulyukin at usu dot edu
####################################

import scipy as sp
from sklearn.feature_extraction.text import CountVectorizer

# create two simple texts
texts = ['How to format my hard disk disk', ' Hard disk format problems problems problems ']
print('text 0: %s' % texts[0])
print('text 1: %s' % texts[1])

# initialiaze & print the vectorizer
vectorizer = CountVectorizer(min_df=1)

#print(vectorizer)

# create a sparse feature matrix
feat_mat = vectorizer.fit_transform(texts)
print type(feat_mat)
print(vectorizer.get_feature_names())
## These are the features:
## [u'disk', u'format', u'hard', u'how', u'my', u'problems', u'to']
## In other words,
## - disk           is      feature 0
## - format       is      feature 1
## - hard          is      feature 2
## - how           is      feature 3
## - my            is      feature 4
## - problems   is     feature 5
## - to              is      feature 6
print '-----------------'
print 'feat_mat'
print(feat_mat)
print '-----------------'
##    3     6      1       4     2     0           2     0        1          5
## ["How to format my hard disk", " Hard disk format problems "]
##  (0, 3)	1 - (0, 3) means - text 0 has feature 3
##  (0, 6)	1 - (0, 6) means - text 0 has feature 6
##  (0, 1)	1 - (0, 1) means - text 0 has feature 1
##  (0, 4)	1 - (0, 4) means - text 0 has feature 4
##  (0, 2)	1 - (0, 2) means - text 0 has feature 2
##  (0, 0)	1 - (0, 0) means - text 0 has feature 0
##  (1, 1)	1 - (1, 1) means - text 1 has feature 1
##  (1, 2)	1 - (1, 2) means - text 1 has feature 2
##  (1, 0)	1 - (1, 0) means - text 1 has feature 0
##  (1, 5)	1 - (1, 5) means - text 1 has feature 5

# let us convert sparse feature matrix to array
print '-----------------'
print 'feat_mat.toarray()'
print feat_mat.toarray()

# let us transpose and print term matrix
print '-----------------'
print 'feat_mat.toarray().transpose()'
print(feat_mat.toarray().transpose())
print '-----------------'

## the above print produces the following output:
## the 0-th column is text 0, the 1-st column is text 1
##                 0           1             2           3        4             5             6
## feats:  [u'disk', u'format', u'hard', u'how', u'my', u'problems', u'to']
## text 0: [1          1          1        1       1       0          1] -
## this means that text 0 contains features 0, 1, 2, 3, 4, and 6 and does
## not contain feature 5, i.e., problems.
## text 1: [1          1          1         0      0       1          0] -
## this means that text 1 contains features 0, 1, 2, 5, and does not
## contain features 3, 4, and 6.
##[[1 1] - 0 document 1 contains features 0, 1, 2, 5; doc 1 contains 
## [1 1] - 1
## [1 1] - 2
## [1 0] - 3
## [1 0] - 4
## [0 1] - 5
## [1 0] - 6
## ]

#new_post = "imaging databases"
#new_post_vec = vectorizer.fit_transform([new_post])
#print(new_post_vec)
