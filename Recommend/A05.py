# 백준 2667번: 단지번호붙이기
# bfs 수행해서 확인

from collections import deque

n = int(input())
graph = [[-1 for _ in range(n+2)]]
for _ in range(n):
    str = input()
    tmp = [-1]
    for c in str:
        tmp.append(int(c))
    tmp.append(-1)
    graph.append(tmp)
graph.append([-1 for _ in range(n+2)])


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    cnt = 0
    while q:
        sx, sy = q.popleft()
        cnt += 1
        for i in range(4):
            cx, cy = sx + dx[i], sy + dy[i]
            if graph[cx][cy] == 1:
                q.append((cx, cy))
                graph[cx][cy] = 0
    return cnt

answer = 0
number = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 1:
            number.append(bfs(i, j))
            answer += 1

print(answer)
number.sort()
for i in number:
    print(i)