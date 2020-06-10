#!/bin/python3

import sys

def sumOfList(n,q):
    p = q-1
    return n*(p//n)*((p//n)+1)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((sumOfList(3, n)+ sumOfList(5, n) - sumOfList(15, n))//2)
