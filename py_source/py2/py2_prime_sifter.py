#!/usr/bin/python

#############################
## module: py2_prime_sifter.py
## author: vladimir kulyukin
## Py2 source for cs3430, S18, lecture 2
## description: sifts primes in a specified range.
#############################

## this is an example of how to re-use our
## newton_sqrt function developed in Lecture 2.
from newton_square_root import newton_sqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for d in xrange(2, int(newton_sqrt(n))+1):
        if n % d == 0:
            return False
    return True

## uncomment this comment if you want to
## use the built-in function math.sqrt.
'''
import math
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for d in xrange(2, int(math.sqrt(n))+1):
        if n % d == 0:
            return False
    return True
'''

def is_prime2(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for d in xrange(2, int(n/2.0)+1):
        if n % d == 0:
            return False
    return True

def sift_primes_in_range(prime_pred, number_range):
    prime_list = []
    for n in number_range:
        if prime_pred(n):
            prime_list.append(n)
    return prime_list

if __name__ == '__main__':
    prime_list_1 = sift_primes_in_range(is_prime, xrange(0, 31))
    print prime_list_1
    prime_list_2 = sift_primes_in_range(is_prime2, xrange(0, 31))
    print prime_list_2
