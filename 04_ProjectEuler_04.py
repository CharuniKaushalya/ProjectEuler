#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    found = False
    str_n = str(n)
    firstHalf = 998
    palin = 0
 
    while (not(found)):
        firstHalf -= 1
        k = str(firstHalf)
        palin = int(k+k[::-1])
        for i in range(999,99,-1):
            if ((palin / i) > 999 or i*i < palin) :
                break
 
            if ((palin % i == 0) and palin < n) :
                found = True
                break
    print(palin)
 