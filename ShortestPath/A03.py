import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    graph[a][a] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

minDist = INF
for i in range(1, n):
    for j in range(i+1, n+1):
        if graph[i][j] != INF and graph[j][i] != INF:
            minDist = min(minDist, graph[i][j] + graph[j][i])
if minDist == INF:
    print(-1)
else:
    print(minDist)