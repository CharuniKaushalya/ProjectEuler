#!/bin/python3

import sys
import math 

def multiplyList(myList) : 
      
    # Multiply elements one by one 
    result = 1
    for x in myList: 
         result = result * x  
    return result 

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    maxPro = 0
    for i in range(n-k):
        lis = list(map(int,num[i:i+k]))
        prod = multiplyList(lis)
        if(prod >maxPro and len(lis) > 0):
            maxPro = prod
    print(maxPro)