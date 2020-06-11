#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = b = 1
    sum = 0
    for i in range(n//2):
        a,b = b,a+b
        if(a>n):
            break
        if(a%2 == 0):
            sum += a
    print(sum)