#!/usr/bin/python

#################################################
# module: tfidf.py
# description: basic implementation of tf and idf
# functions.
#
# bugs to vladimir dot kulyukin at usu dot edu
#################################################

import scipy as sp

# how frequent term t is in document docs
def term_freq(t, doc):
    # sum the occurrences of all terms in doc
    n = sum(doc.count(term) for term in set(doc))
    # compute the occurences of term t in doc
    tf = float(doc.count(t))
    # normalize tf by n
    print('n = %d, tf = %f' % (n, tf))
    return tf/n

def inverse_doc_freq(t, docset):
    num_docs = len(docset)
    num_docs_with_t = len([doc for doc in docset if t in doc])
    return sp.log(float(num_docs)/num_docs_with_t)

def tfidf(t, doc, docset):
    tf = term_freq(t, doc)
    idf = inverse_doc_freq(t, docset)
    return tf*idf

## three are documents in our toy collection: A, ABB, ABC
A, ABB, ABC = ['a'], ['a', 'b', 'b'], ['a', 'b', 'c']
## DOCSET is a document collection; we assume that
## DOCSET is immutable
DOCSET = (A, ABB, ABC)

def unit_test_01():
    print term_freq('a', A)
    print term_freq('a', ABB)
    print term_freq('b', ABC)

def unit_test_02():
    print inverse_doc_freq('a', DOCSET)
    print inverse_doc_freq('b', DOCSET)
    print inverse_doc_freq('c', DOCSET)

def unit_test_03():
    print("tfidf('a', a, D)\t=\t%f" % tfidf('a', A, DOCSET))
    print("tfidf('b', abb, D)\t=\t%f" % tfidf('b', ABB, DOCSET))
    print("tfidf('a', abc, D)\t=\t%f" % tfidf('a', ABC, DOCSET))
    print("tfidf('c', abc, D)\t=\t%f" % tfidf('c', ABC, DOCSET))
