#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    position = 0
    jump = 0

    while True:
        if position + 2 >= len(c) -1:
            jump+= 1
            break

        if c[position+2] != 1:
            position += 2
            jump += 1
        else:
            position += 1
            jump += 1

    return jump        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
