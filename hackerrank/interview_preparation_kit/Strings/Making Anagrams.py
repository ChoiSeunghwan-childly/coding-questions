#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_idx = 0
    b_idx = 0
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    count = 0

    while True:
        if a_sorted[a_idx] == b_sorted[b_idx]:
            a_idx += 1
            b_idx += 1
        elif a_sorted[a_idx] < b_sorted[b_idx]:
            a_idx += 1
            count += 1
        elif a_sorted[a_idx] > b_sorted[b_idx]:
            b_idx += 1
            count += 1
    
        if a_idx == len(a_sorted):
            count += len(b_sorted) - b_idx
            break
        elif b_idx == len(b_sorted):
            count += len(a_sorted) - a_idx
            break
    
    return count
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
