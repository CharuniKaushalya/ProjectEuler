#!/bin/python3

import sys
import math

def gcd(a, b) :
    y = 0
    x = 0
 
    if(a > b):
        x = a
        y = b
    else:
        x = b
        y = a
 
    while (x % y != 0):
        temp = x
        x = y
        y = temp % x
    return y


t = int(input().strip())
for a0 in range(t):
    s = int(input().strip())
    a=b=c=0
    m = k = n = d = 0
    found= False
 
    mlimit = int(math.sqrt(s / 2))
    for m in range(2,mlimit+1):
        if((s / 2) % m == 0): 
            if(m % 2 == 0):
                k = m + 1
            else:
                k = m + 2
            while(k < 2 * m and k <= s / (2 * m)):
                if(s / (2 * m) % k == 0 and gcd(k, m) == 1):
                    d = s / 2 / (k * m)
                    n = k - m
                    a = d*(m * m - n * n)
                    b = 2 * d * n * m
                    c = d * (m * m + n * n)
                    found = True
                    break
                k += 2
        if(found):
            print(int(a*b*c))
            break
    else:  # Executed because no break in for 
        print(-1) 
  
            
