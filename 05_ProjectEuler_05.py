#!/bin/python3

import sys
import math

thisdict = {2: 0,3: 0,5: 0,7:0,11:0,13:0,17:0,19:0,23:0,29:0}


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(2,n+1):
        for k,v in thisdict.items():
            # print(i,k,v)
            if(i%k == 0):
                mat = math.floor(math.log(i, k))
                # print("got mat", i,k,v,mat)
                if(mat > v):
                    thisdict[k] = mat
    tot = 1
    for k,v in thisdict.items():
        if(v != 0):
            tot *= pow(k,v)
    print(tot)