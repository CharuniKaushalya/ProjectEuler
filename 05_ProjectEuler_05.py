#!/bin/python3

import sys
import math

# returns smallest multiple that is evenly divisible by all numbers from 1 - n
# returns -1 if multiple does not exist
def findSmallestMultiple(n):
    for i in range(n, factorial(n) + 1, n):
        if isMultiple(i, n):
            return i
    return -1

# checks every number between 1 and n to see if x is a multiple of every number
# returns True if x is found to be a multiple of every number, and False if x is
# found to not be a multiple of any number
def isMultiple(x, n):
    for i in range(1, n):
        if x % i != 0:
            return False
    return True

# returns the n factorial, or -1 if it does not exist
def factorial(n):
    if n > 1: return n * factorial(n - 1)
    elif n >= 0: return 1
    else: return -1



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(findSmallestMultiple(n))