# 2675 - 문자열 반복


def solution(N):
    for i in range(N):
        R, S = input().split(" ")
        R = int(R)

        resultStr = ""
        for j in range(len(S)):
            resultStr += S[j] * R
        print(resultStr)


N = int(input())
solution(N)