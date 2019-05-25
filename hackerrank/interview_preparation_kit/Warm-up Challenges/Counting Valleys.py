#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    horizon = 0
    flag = None
    

    for ch in s:
        if ch == 'U':
            horizon += 1
        else:
            horizon -= 1
        if horizon == 0 and ch == 'U':
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
