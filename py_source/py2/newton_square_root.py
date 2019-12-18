#!/usr/bin/python

## if you do not want to import division,
## you have to do float(x) and (x+y)/2.0,
## as is done in the slides.

from __future__ import division

###############################
## module: newton_square_root.py in Py2
## author: vladimir kulyukin
## description: function newton_sqrt(n) computes
## newton's square root appproximation of n.
###############################

## computes the average of x and y
def average(x, y):
    '''computes the average of x and y'''
    return (x + y)/2

def next_guess(n, g):
    '''computes next guess in newton's sqrt approx'''
    return average(g, n/g)

def is_good_enough(n, g, error=0.00001):
    return abs(g**2 - n) <= error

def newton_square_root(n, g, error):
    if is_good_enough(n, g, error):
        return g
    else:
        #ng = next_guess(n, g)
        return newton_square_root(n,
                                  next_guess(n, g),
                                  error)

def newton_sqrt(n):
    return newton_square_root(n, 1, 0.00001)

## print square roots of numbers in [0, 10]
## by the way, if you want to be forward-compatible
## with Py3, do
## from __future__ import print_function
if __name__ == '__main__':
    for i in xrange(11):
        print newton_sqrt(i)

