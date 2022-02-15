from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    move = deque()
    deq.append([x, y])
    check[x][y] = 1
    people, cnt = 0, 0
    while deq:
        x, y = deq.popleft()
        move.append([x, y])
        people += a[x][y]
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not check[nx][ny]:
                if l <= abs(a[x][y] - a[nx][ny]) <= r:
                    check[nx][ny] = 1
                    deq.append([nx, ny])

    while move:
        x, y = move.popleft()
        a[x][y] = people // cnt

    if cnt == 1:
        return 0
    return 1

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

day = 0
while True:
    deq = deque()
    check = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                cnt += bfs(i, j)
    if not cnt:
        break
    day += 1

print(day)