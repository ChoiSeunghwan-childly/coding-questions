mem = []
for i in range(100):
    mem.append(0)

def fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        if mem[n] != 0:
            return mem[n]
        else:
            mem[n] = fibo(n-1) + fibo(n-2)
            return mem[n]
        
n = int(input())
print(fibo(n))