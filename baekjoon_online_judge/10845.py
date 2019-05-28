class _Queue:
    def __init__(self):
        self.q = []
    
    def push(self, x):
        self.q.append(x)
        

    def pop(self):
        if len(self.q) == 0:
            return -1
        else:
            return self.q.pop(0)

    def size(self):
        return len(self.q)

    def empty(self):
        if len(self.q) == 0:
            return 1
        else: return 0

    def front(self):
        if self.empty():
            return -1
        else:
            return self.q[0]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.q[-1]

q = _Queue()
N = int(input())
for _ in range(N):
    cmd = input().split(' ')
    if cmd[0] == 'push':
        q.push(cmd[1])
    elif cmd[0] == 'pop':
        print(q.pop())
    elif cmd[0] == 'size':
        print(q.size())
    elif cmd[0] == 'empty':
        print(q.empty())
    elif cmd[0] == 'front':
        print(q.front())
    elif cmd[0] == 'back':
        print(q.back())
