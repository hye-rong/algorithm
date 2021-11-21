# 백준 1766번: 문제집
from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())
edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

heap = []

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    edges[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for i in edges[data]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)

for i in result:
    print(i, end=' ')