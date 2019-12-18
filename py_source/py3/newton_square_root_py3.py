#!/usr/bin/python3

## No need for this import any more, because
## were in Py3: float division is default
## from __future__ import division

#######################
## module: newton_square_root_py3.py in Py3
## author: vladimir kulyukin
## computes newton's square root appproximation
########################

def average(x, y):
    return (x + y)/2

def next_guess(n, g):
    return average(g, n/g)

def is_good_enough(n, g, error):
    return abs(g**2 - n) <= error

def newton_square_root(n, g, error):
    if is_good_enough(n, g, error):
        return g
    else:
        return newton_square_root(n,
                                  next_guess(n, g),
                                  error)

def newton_sqrt(n):
    return newton_square_root(n, 1, 0.00001)

## let's print square roots of numbers in [0, 10]
## xrange in Py2 is the same as range in Py3
if __name__ == '__main__':
    for i in range(11):
        print(newton_sqrt(i))

