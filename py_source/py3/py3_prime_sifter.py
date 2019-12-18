#!/usr/bin/python3

#############################
## module: py3_prime_sifter.py
## author: vladimir kulyukin
## Py3 source for cs3430, S18, lecture 2
## description: sifts primes in a specified range.
#############################

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for d in range(2, int(math.sqrt(n))+1):
        if n % d == 0:
            return False
    return True

def is_prime2(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for d in range(2, int(n/2)+1):
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
    prime_list_1 = sift_primes_in_range(is_prime, range(0, 31))
    print(prime_list_1)

    prime_list_2 = sift_primes_in_range(is_prime2, range(0, 31))
    print(prime_list_2)

    
