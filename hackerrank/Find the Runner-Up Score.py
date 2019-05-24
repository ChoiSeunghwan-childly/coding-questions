if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    print(arr)

    maxNum = arr[0]
    for i in range(1 , len(arr)):
        if maxNum > arr[i]:
            print(arr[i])
            break