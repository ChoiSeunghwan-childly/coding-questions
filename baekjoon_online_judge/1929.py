# 1929 - 소수 구하기 (일반적인 방법, 업그레이드, 에라스토테네스의 체)
import time


def commonSolution(N, M):
    for i in range(N, M + 1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            print(i)


def upgradeSolution(N, M):
    startTime = time.time()
    primeList = list()

    primeList.append(2)

    for num in range(N, M+1):
        isPrime = True
        for pNum in primeList:
            if (num % pNum ) == 0:
                isPrime = False
                break
        if isPrime:
            primeList.append(num)

    # for item in primeList:
    #     print(item)

    print(time.time() - startTime)


def erasthos(N ,M):
    # startTime = time.time()
    numAry = [False] * (M + 2)
    pList = list()

    for i in range(2, M  +1):
        if (numAry [i] == False):
            pList.append(i)
            numAry[i] = True
            for j in range(i + i, M + 1, i):
                numAry[j] = True

    #print(pList)
    # print(time.time() - startTime)
    for item in pList:
        if (item >= N) & (item <= M):
            print(item)

N, M = map(int, input().split())
#upgradeSolution(N, M)
erasthos(N ,M)
