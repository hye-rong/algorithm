# 백준 2693번: N번째 큰 수

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quickSort(left) +[pivot] + quickSort(right)

t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    b = quickSort(a)
    print(b[-3])