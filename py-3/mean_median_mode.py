#!/usr/bin/python

#######################################
# module: mean_median_mode.py
# author: vladimir kulyukin
# description: computing and plotting
# means, medians, and modes.
#######################################

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

## use normal distribution to generate 10,000 points
## centered on 30,000 with an STD = 15,000
incomes = np.random.normal(30000, 15000, 10000)
## if you want to see an outlier, add this
## billionaire's income to the list of incomes
#incomes = np.append(incomes, [1000000000])

mn = np.mean(incomes)
print('mean    = ' + str(mn))
md = np.median(incomes)
print('median = ' + str(md))

## comment out if you don't want to see a plot of incomes
plt.hist(incomes, 50)
plt.show()

## create a random array of 500 ages from 10 up to 90.
ages = np.random.randint(10, high=90, size=500)
print(ages)
mo = stats.mode(ages)
## the result will print like (array([ 22.]), array([ 18.])),
## where the first number, 22, is the most frequent age
## and the second number, 18, is the number of times
##that age occurs in ages.
print(mo)
