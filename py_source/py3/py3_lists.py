#!/usr/bin/python3

#############################
## module: py3_lists.py
## author: vladimir kulyukin
## Py3 source for cs3430, S18, lecture 2
#############################

## destructive modification of lists
def sqrt_list(a_list):
    for i in range(len(a_list)):
        a_list[i] **= 0.5

## constructive modification of lists
## by making shallow copies.
## uncomment the statements below
## to see the output.
import copy

def sqrt_list_copy(a_list):
    shallow_copy = copy.copy(a_list)
    for i in range(len(a_list)):
        shallow_copy[i] **= 0.5
    return shallow_copy

if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    print(lst)
    sqrt_list(lst)
    print(lst)
    lst = [1, 2, 3, 4]
    print(lst)
    sqrt_of_lst = sqrt_list_copy(lst)
    print(sqrt_of_lst)
    print(lst)

