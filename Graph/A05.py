# 백준 2178번: 미로탐색
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input() for _ in range(n)]
check = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


q = deque()
# bfs 수행
q.append([0, 0, 1]) # i, j, count
check[0][0] = 1
while q:
    x, y, count = q.popleft()
    if x == n-1 and y == m-1:
        print(count)
        break
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if 0 <= cx < n and 0 <= cy < m:
            if graph[cx][cy] == '1' and check[cx][cy] == 0:
                q.append([cx, cy, count+1])
                check[cx][cy] = 1


