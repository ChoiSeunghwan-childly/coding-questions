stack = list()

def push(item):
    stack.append(item)

def pop():
    if len(stack) > 0:
        return stack.pop()
    else:
        return "EMPTY"

def solution(s):
    for ch in s:
        if ch == '(':
            push(ch)
        elif ch == ')':
            item = pop()
            if item == 'EMPTY':
                return 'NO'
                
    if len(stack) > 0:
        return 'NO'
    return 'YES'

N = int(input())
results = []
for _ in range(N):
    stack.clear()
    s = input()
    result = solution(s)
    results.append(result)

for result in results:
    print(result)