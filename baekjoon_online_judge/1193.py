# 분수찾기 성공
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 0.5 초 (언어별 추가 시간 없음)	256 MB	16879	8533	7613	54.371%
# 문제
# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

# 1/1	1/2	1/3	1/4	1/5	…
# 2/1	2/2	2/3	2/4	…	…
# 3/1	3/2	3/3	…	…	…
# 4/1	4/2	…	…	…	…
# 5/1	…	…	…	…	…
# …	…	…	…	…	…
# 이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

# 출력
# 첫째 줄에 분수를 출력한다.

# 예제 입력 1 
# 14
# 예제 출력 1 
# 2/4


limit = 2
count = 2
nuNum = 1   #numerator 분자 
deNum = 2   #denominator 분모
n = 0

def checkCount():
    global nuNum, limit, deNum, n, count

    if n == count:
        print(str(nuNum) + '/' + str(deNum))
        return True
    return False


def solution():
    global nuNum, limit, deNum, n, count

    if n == 1:
        print("1/1")
        return True
    elif n == 2:
        print("1/2")
        return True

    while True:
        while nuNum < limit:
            nuNum += 1
            deNum -= 1
            count += 1
            if checkCount():
                return True

        limit += 1
        nuNum += 1
        count += 1
        if checkCount():
            return True

        while deNum < limit:
            nuNum -= 1
            deNum += 1
            count += 1
            if checkCount():
                return True
        limit += 1
        deNum += 1
        count += 1
        if checkCount():
            return True
        
            
def solution2(n):
    group = 0
    sum = 0
    while n > sum: 
        group += 1
        sum += group
    
    if group % 2 == 0:
        bhunza = group - ( sum - n)
        bhunmo = 1 + ( sum - n )
    else:
        bhunza = 1 + ( sum - n)
        bhunmo = group - ( sum - n)
        
        
    print(str(bhunza) +'/' + str(bhunmo))


if __name__ == "__main__":
    n = int(input())
    #solution1() 시간초과...;;
    solution2(n)