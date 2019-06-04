#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(reverse = True)
    count = 0
    luck_sum = 0


    for i in range(len(contests)):
        if contests[i][1] == 1 and count >= k:
            luck_sum -= contests[i][0]
        elif contests[i][1] == 1 and count < k:
            count += 1
            luck_sum += contests[i][0]
        else:
            luck_sum += contests[i][0]

    return luck_sum
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
