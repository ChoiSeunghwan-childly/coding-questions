#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    sorted_arr = sorted(arr)
    min_abs = abs(sorted_arr[0] - sorted_arr[1])

    for i in range(1, len(sorted_arr)- 1):
        val = abs(sorted_arr[i] - sorted_arr[i+1])
        if val < min_abs:
            min_abs = val

    return min_abs
    

    # Time out.
    # for i in range(len(arr)):
    #     for j in range(i + 1, len(arr)):
    #         val = abs(arr[i]-arr[j])
    #         if val < min_abs:
    #             min_abs = val
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
