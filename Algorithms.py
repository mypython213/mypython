import time
from  matplotlib import pyplot
import random

import math

def measure (n,k, fn):
    start = time.time()
    for i in range(k):
        fn(n)
    end = time.time()
    return (end - start)


def binary_search (n:[]):
    left = 0
    right = len(n)
    middle = 0
    while (left<=right):
        middle = (left+right)//2
        if n[-1] < n[middle]:
            right = middle -1
        elif n[-1] > n[middle]:
            left = middle + 1
        else:
            return middle
    return None

def lenear_search(n:[]):
    for i in n:
        if i==n[-1]:
            return i
    return None

def bubble_sort(n:[]):
    for i in range(len(n)):
        for j in range(i, len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]
    return n

# print (binary_search([1,2,3,4,5,6,7]))

myf = lambda x: '*'*x
mf_const = lambda x: '*'
mf_log = lambda x: math.log10(x)
mf_lsearch = lambda x: lenear_search(range(x))
mf_bsearch = lambda x: binary_search(range(x))
mf_bsort = lambda x: bubble_sort(range(x))

# print (measure(100000,100,myf))

# print(mf_lsearch(10))
axes_x = []
axes_y_sqr = []
axes_y_const = []
axes_y_log = []
axes_y_lsearch = []
axes_y_bsearch = []
axes_y_bsort = []
for i in range(50):
    axes_y_sqr.append (measure(100000, i * 10, myf))
    axes_y_const.append (measure(100000, i * 10, mf_const))
    axes_y_log.append (measure(100000, i * 10, mf_log))
    axes_y_lsearch.append (measure(100, i*10 , mf_lsearch))
    axes_y_bsearch.append (measure(100, i*10 , mf_bsearch))
    axes_y_bsort.append (measure(100, i*10 , mf_bsort))
    axes_x.append(i)
pyplot.plot(axes_x, axes_y_sqr)
pyplot.plot(axes_x, axes_y_const)
pyplot.plot(axes_x, axes_y_log)
pyplot.plot(axes_x, axes_y_lsearch)
pyplot.plot(axes_x, axes_y_bsearch)
pyplot.plot(axes_x, axes_y_bsort)
pyplot.legend(["sqr",'const', 'log', 'lsearch','mf_bsearch', 'bsort'])
pyplot.show()


