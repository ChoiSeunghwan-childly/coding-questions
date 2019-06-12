import random

arr = [random.randint(0, 100) for k in range(20)]
print(arr)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def bubbleSort(arr):
    for size in reversed(range(len(arr))):
        for i in range(size):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)

def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                swap(arr, i, j)

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)
            else: break

def partition(arr, low, high):
    i = ( low - 1 )
    pivot = arr[high]

    for j in range(low , high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1] , arr[high] = arr[high], arr[i+1]
    return ( i+1 )

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

insertionSort(arr)
print(arr)