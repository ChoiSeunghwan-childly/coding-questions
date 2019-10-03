import itertools as it

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    
    for i in range(2, num):
        if num%i == 0:
            return False
    return True
        
def solution(arg):
    numbers = list(arg)
    primeList = []
    
    for i in range(1, len(numbers)+1):
        itList = it.permutations(numbers, i)
        for per in itList:
            num = ''
            for ch in per:
                num += ch
            if(int(num) not in primeList and isPrime(int(num))):
                primeList.append(int(num)) 
    
    return len(primeList)