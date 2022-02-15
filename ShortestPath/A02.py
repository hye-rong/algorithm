import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 처리한 노드
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(1)

maxDist, index, num = 0, 0, 0
for i in range(1, n+1):
    if distance[i] == INF:
        continue
    if distance[i] > maxDist:
        maxDist = distance[i]
        index = i
        num = 1
    elif distance[i] == maxDist:
        num += 1
print("{0} {1} {2}".format(index, maxDist, num))