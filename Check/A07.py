# 백준 1916번: 최소비용 구하기
import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

s, e = map(int, input().split())

INF = 1e9
dist = [INF for _ in range(n+1)]
dist[s] = 0

q = []
heapq.heappush(q, (0, s))
while q:
    d, cur = heapq.heappop(q)
    if dist[cur] < d: # 갱신이 안되는 경우
        continue
    for i in graph[cur]: # 해당 노드에서 갈 수 있는 노드 확인
        cost = d + i[1]
        if dist[i[0]] > cost:
            dist[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
print(dist[e])
