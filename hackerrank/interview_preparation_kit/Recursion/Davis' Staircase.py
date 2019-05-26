#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
mem = []

def stepPerms(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        if mem[n] == 0:
            mem[n] = stepPerms(n-1) + stepPerms(n-2) +\
                    stepPerms(n-3)
        return mem[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())
        mem = [0] * (n+1)
        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
