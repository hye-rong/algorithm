# 백준 1303번: 전쟁 - 전투

from collections import deque

m, n = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, c):
    q = deque()
    q.append((x, y))
    answer = 0
    while q:
        a, b = q.popleft()
        answer += 1
        for i in range(4):
            cx, cy = a + dx[i], b + dy[i]
            if 0 <= cx < n and 0 <= cy < m:
                if graph[cx][cy] == c and visited[cx][cy] == 0:
                    q.append((cx, cy))
                    visited[cx][cy] = 1
    return answer

result = [0, 0]
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            visited[i][j] = 1
            c = graph[i][j]
            k = bfs(i, j, c)
            if c == 'W':
                result[0] += k*k
            else:
                result[1] += k*k
for i in result:
    print(i, end=' ')