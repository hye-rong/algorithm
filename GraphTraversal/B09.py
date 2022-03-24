# 백준 17869번: 아기 상어 2
# 상어 위치를 모두 찾음
# bfs를 통해서 하나씩 늘려서 값 저장

from collections import deque

n, m = map(int, input().split())

graph = [[-1 for _ in range(m+2)]]
shark = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 1:
            shark.append((i+1, j+1))
    graph.append([-1] + tmp + [-1])
graph.append([-1 for _ in range(m+2)])

dx = [0, 1, 0, -1, -1, -1, 1, 1]
dy = [1, 0, -1, 0, -1, 1, -1, 1]


def bfs(sh):
    q = deque()
    for s in sh:
        q.append((s[0], s[1], 0))

    while q:
        a, b, c = q.popleft()
        for k in range(8):
            cx, cy = a + dx[k], b + dy[k]
            if graph[cx][cy] == 0:
                graph[cx][cy] = c + 1
                q.append((cx, cy, c+1))

    print(max(map(max, graph)))


bfs(shark)

