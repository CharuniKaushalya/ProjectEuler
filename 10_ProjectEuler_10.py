#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    primes = [2]
    for x in range(3,n+1):
        isPrime = True
        i = 2
        while (i*i <= n):
            if (x % i== 0):
                isPrime = False
                break
            else:
                i += 1

        if (isPrime): # the remainder is a prime number
            print(x)
            primes.append(x)
    print(sum(primes))

