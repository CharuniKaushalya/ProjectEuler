    #!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    largestFact = 0
    i = 2
    newnum = n
    while (i * i <= n):
        if (newnum % i == 0):
            newnum = newnum // i
            largestFact = i
        else:
            i += 1

    if (newnum > largestFact): # the remainder is a prime number
        largestFact = newnum
    print(largestFact)

