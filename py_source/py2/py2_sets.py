#!/usr/bin/python

#############################
## module: py2_sets.py
## author: vladimir kulyukin
## Py2 source for cs3430, S18, lecture 2
#############################

## destructive modification of sets
def remove_from_set(x, a_set):
    if x in a_set:
        a_set.remove(x)

## constructive modification of sets
## we make a shallow copy of a list
## by calling copy member function.
## uncomment the statements below
## to see the output
def remove_from_set_copy(x, a_set):
    shallow_copy = a_set.copy()
    if x in a_set:
        shallow_copy.remove(x)
        return shallow_copy
    else:
        return shallow_copy

if __name__ == '__main__':
    s = set((1, 2, 3, 4))
    print s
    remove_from_set(3, s)
    print s
    remove_from_set(10, s)
    print s
    s = set([1, 2, 3, 4])
    print s
    copy_of_s = remove_from_set_copy(2, s)
    print copy_of_s
    print s

