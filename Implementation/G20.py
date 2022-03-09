# 백준 17276번: 배열 돌리기
# 하나씩 줄을 세워서 어느 줄에 들어갈지 계산해서 넣어줌
# 기존의 배열이 바꾸지 않도록 깊은 복사 수행
# 해설을 보니 빼서 넣는 코드는 45도 회전만 하고 그 코드를 반복하기도 함


import sys
import copy

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    d = (d + 360) % 360
    before = [list(map(int, input().split())) for _ in range(n)]
    new = copy.deepcopy(before)
    for i in range(4):
        k = (i + d/45) % 8
        tmp = []
        if i == 0:
            for j in range(n):
                tmp.append(before[n // 2][j])
        elif i == 1:
            for j in range(n):
                tmp.append(before[j][j])
        elif i == 2:
            for j in range(n):
                tmp.append(before[j][n // 2])
        elif i == 3:
            for j in range(n):
                tmp.append(before[j][n-j-1])

        if k > 3:
            tmp.reverse()
        k = k % 4
        if k == 0:
            for j in range(n):
                new[n // 2][j] = tmp[j]
        elif k == 1:
            for j in range(n):
                new[j][j] = tmp[j]
        elif k == 2:
            for j in range(n):
                new[j][n // 2] = tmp[j]
        elif k == 3:
            for j in range(n):
                new[j][n-j-1] = tmp[j]

    for i in range(n):
        for j in range(n):
            print(new[i][j], end=' ')
        print()



