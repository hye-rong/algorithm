import collections
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
road_list = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    road_list[a].append(b)
dist = [-1] * (n+1)
dist[x] = 0

dequedata = collections.deque([x])

while dequedata:
    node = dequedata.popleft()
    if dist[node] < k:
        for i in road_list[node]:
            if dist[i] == -1:
                dist[i] = dist[node] + 1
                dequedata.append(i)

check = False
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        check = True
if check==False:
    print(-1)