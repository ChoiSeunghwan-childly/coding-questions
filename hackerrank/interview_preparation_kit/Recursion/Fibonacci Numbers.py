mem = []

def fibonacci(n):
    if n < 2:
        return n
    
    if mem[n] == 0:
        mem[n] = fibonacci(n-1) + fibonacci(n-2)
        return mem[n]
    else:
        return mem[n]
    # Write your code here.

n = int(input())
mem = (n+1) * [0]
print(fibonacci(n))

