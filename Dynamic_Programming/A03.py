# 백준 18353번: 병사 배치하기

def binary_search(num, l):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end)//2
        if l[mid] > num:
            start = mid + 1
        else:
            end = mid - 1
    return start


n = int(input())
s = list(map(int, input().split()))
l = [s[0]]

for i in range(1, n):
    idx = binary_search(s[i], l)
    if len(l) > idx:
        l[idx] = s[i]
    else:
        l.append(s[i])

print(n - len(l))