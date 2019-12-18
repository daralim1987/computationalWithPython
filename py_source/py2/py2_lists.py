#!/usr/bin/python

#############################
## module: py2_lists.py
## author: vladimir kulyukin
## Py2 source for cs3430, S18, Lecture 2
#############################

import copy

## destructive modification of lists
def sqrt_list(a_lst):
    for i in xrange(len(a_lst)):
        a_lst[i] **= 0.5

## constructive modification of lists
## uncomment the statements below
## to see the output
def sqrt_list_copy(a_list):
    shallow_copy = copy.copy(a_list)
    for i in xrange(len(shallow_copy)):
        shallow_copy[i] **= 0.5
    return shallow_copy

if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    print lst
    sqrt_list(lst)
    print lst
    lst = [1, 2, 3, 4]
    print lst
    print sqrt_list_copy(lst)
    print lst
