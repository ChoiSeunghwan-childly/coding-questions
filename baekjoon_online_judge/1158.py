# 조세퍼스 문제
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	256 MB	16396	8222	6175	51.961%
# 문제
# 조세퍼스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 M(≤ N)이 주어진다. 이제 순서대로 M번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, M)-조세퍼스 순열이라고 한다. 예를 들어 (7, 3)-조세퍼스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
# N과 M이 주어지면 (N,M)-조세퍼스 순열을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 M이 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ M ≤ N ≤ 5,000)

# 출력
# 예제와 같이 조세퍼스 순열을 출력한다.

# 예제 입력 1
# 7 3
# 예제 출력 1
# <3, 6, 2, 7, 5, 1, 4>
import queue
import collections


def sol1():  # nList.pop(0) 은 O(n) 번 만큼의 대이동. 시간초과
    nList = [i + 1 for i in range(N)]

    while len(nList) > 0:
        for i in range(M - 1):
            item = nList.pop(0)
            nList.append(item)
        resultList.append(nList.pop(0))


def sol2():  # queue 이용. 시간초과 (원형큐로 직접 구현해서 푸는 방법이 많았음. queue 모듈은 뭔가 다른 용도인 듯.)
    q = queue.Queue()

    for i in range(N):
        q.put(i + 1)
    while q.qsize() > 0:
        for i in range(M - 1):
            q.put(q.get())
        resultList.append(q.get())


def sol3():  # 정답. 콜렉션의 deque 자료구조 이용하여 해결. queue를 직접 구현하긴 스마트하지 않아...
    d = collections.deque([i + 1 for i in range(N)])
    while len(d) > 0:
        for i in range(M - 1):
            d.append(d.popleft())
        resultList.append(d.popleft())


N, M = map(int, input().split())
resultList = list()

sol3()
print('<', end='')
print(*resultList, sep=', ',end='')
print('>')
