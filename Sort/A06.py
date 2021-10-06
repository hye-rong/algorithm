# 백준 5052번 : 전화번호 목록

import sys
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    num = [sys.stdin.readline().strip() for _ in range(n)]
    num.sort()
    check = True
    for j in range(n - 1):
        m = min(len(num[j]), len(num[j + 1]))
        if num[j][:m] == num[j + 1][:m]:
            print("NO")
            check = False
            break
    if check:
        print("YES")



