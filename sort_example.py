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

insertionSort(arr)
print(arr)