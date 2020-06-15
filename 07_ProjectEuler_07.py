#!/bin/python3

import sys
primes = [2]
newnum = 1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while (len(primes) <= n):
        isPrime = True
        i = 0
        newnum += 2
        while (primes[i]*primes[i] <= newnum):
            if (newnum % primes[i] == 0):
                isPrime = False
                break
            else:
                i += 1

        if (isPrime): # the remainder is a prime number
            primes.append(newnum)
    print(primes[n-1])

