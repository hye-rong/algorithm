# 백준 2309번: 일곱난쟁이
import itertools
s = 0
arr = []
for i in range(9):
    k = int(input())
    s += k
    arr.append(k)

s -= 100
nCr = itertools.combinations(arr, 2)
for i in nCr:
    a, b = i
    if a+b == s:
        arr.remove(a)
        arr.remove(b)
        break
arr.sort()
for i in arr:
    print(i)
