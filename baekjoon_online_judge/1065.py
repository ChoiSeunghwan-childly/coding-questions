# 한수 성공
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	128 MB	29971	13193	11358	44.494%
# 문제
# 어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

# 예제 입력 1 
# 110
# 예제 출력 1 
# 99
# 예제 입력 2 
# 1
# 예제 출력 2 
# 1
# 예제 입력 3 
# 210
# 예제 출력 3 
# 105
# 예제 입력 4 
# 1000
# 예제 출력 4 
# 144

def solution(n):
    result = 0

    if n < 100:
        return n

    for i in range(100, n+1):
        num = i
        diff = (num % 10) - ( (num // 10) % 10)
        num = num // 10
        flag = 1
        while num:
            a = num % 10
            num = num // 10

            if num == 0:
                break

            b = num % 10
            if a - b != diff:
                flag = 0
                break
        result += flag

    result += 99
    return result


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
    