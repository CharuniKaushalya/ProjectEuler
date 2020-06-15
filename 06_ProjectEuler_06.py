#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sSum = (n*(n+1)*(2*n +1))//6
    sumS = ((n*(n+1))**2)//4
    print(sumS-sSum)