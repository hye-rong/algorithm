# 백준 3460번: 이진수

t = int(input())

for i in range(t):
    n = int(input())
    a = []
    while True:
        a.append(n % 2)
        n = n//2
        if n == 1:
            a.append(1)
            break
        elif n == 0:
            break
    for j in range(len(a)):
        if a[j] == 1:
            print(j, end=' ')
    print()