    #!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    largestFact = 0
    i = 2
    newnumm = n
    while (i * i <= n):
        if (newnumm % i == 0):
            newnumm = newnumm // i
            largestFact = i
        else:
            i += 1

    if (newnumm > largestFact): # the remainder is a prime number
        largestFact = newnumm
    print(largestFact)

