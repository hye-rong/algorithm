# 백준 10818번: 최소, 최대

n = int(input())
a = list(map(int, input().split()))

def quickSort(l):
    if len(l) <= 1:
        return l
    pivot = l[0]

    left = [x for x in l[1:] if x <= pivot]
    right = [x for x in l[1:] if x > pivot]

    return quickSort(left) + [pivot] + quickSort(right)

b = quickSort(a)
print(b[0], b[-1])