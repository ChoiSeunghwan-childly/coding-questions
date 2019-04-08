# 10828 - 스택

stack = list()


def push(x):
    stack.append(x)
    pass


def pop():
    if stack.__len__() == 0:
        print(-1)
    else:
        print(stack.pop())
    pass


def size():
    print(stack.__len__())
    pass


def empty():
    if(stack.__len__() == 0):
        print(1)
    else:
        print(0)
    pass


def top():
    if stack.__len__() == 0:
        print(-1)
    else:
        print(stack[stack.__len__()-1])
    pass


def main():
    n = int(input())
    for i in range(0, n):
        cmd = input().split()

        if cmd[0] == "push":
            push(int(cmd[1]))
        elif cmd[0] == "pop":
            pop()
        elif cmd[0] == "size":
            size()
        elif cmd[0] == "empty":
            empty()
        elif cmd[0] == "top":
            top()
    pass


if __name__ == "__main__":
    main()
else:
    pass
