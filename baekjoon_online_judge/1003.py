# 1003 - 피보나치 함수 (동적 계획법)

memo = [0] * 41
def fibo(n):
    global count0
    global count1
    if n == 0:
        memo[n] = n
        return memo[n]

    elif n == 1:
        memo[n] = n
        return memo[n]

    else:
        if memo[n] > 0:
            return memo[n]
        else:
            memo[n] = fibo(n-1) + fibo(n-2)
            return memo[n]

T = int(input())
for i in range(T):
    num = int(input())
    fibo(num)
    if(num == 0):
        print("1 0")
    elif(num == 1):
        print("0 1")
    else:
        print(memo[num-1], memo[num])