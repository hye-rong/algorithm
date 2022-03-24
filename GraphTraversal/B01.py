# 백준 1260번: DFS와 BFS
import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
edges = [list() for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
for i in range(1, n+1):
    edges[i].sort()

resultD = []
resultB = []
visitedD = [0 for _ in range(n + 1)]
visitedB = [0 for _ in range(n + 1)]


def dfs(x):
    resultD.append(x)
    for i in edges[x]:
        if not visitedD[i]:
            visitedD[i] = 1
            dfs(i)


def bfs(x):
    q = deque()
    q.append(x)
    while q:
        a = q.popleft()
        resultB.append(a)
        for i in edges[a]:
            if not visitedB[i]:
                visitedB[i] = 1
                q.append(i)


visitedD[v] = 1
visitedB[v] = 1
dfs(v)
bfs(v)
for i in resultD:
    print(i, end=' ')
print()
for i in resultB:
    print(i, end=' ')
