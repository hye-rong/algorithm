# 백준 2501번: 약수 구하기

n, k = map(int, input().split())
a = []
b = []
cur = 1
while True:
    if n % cur == 0:
        if cur > n / cur:
            break
        elif cur == n / cur:
            a.append(cur)
            break
        a.append(cur)
        b.append(n//cur)
    if cur >= n / cur:
        break
    cur += 1

if len(a) + len(b) >= k:
    if k-1 < len(a):
        print(a[k-1])
    else:
        print(b[len(a)+len(b)-k])
else:
    print(0)
