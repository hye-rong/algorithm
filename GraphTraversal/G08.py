# 백준 7576번: 토마토
# 최소 시간을 걸리는 문제이므로 BFS 너비우선탐색을 수행
# 인덱스 계산 꼼꼼하게 하기..
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
graph = [[-1] + list(map(int, input().split())) + [-1] for _ in range(n)]
graph.insert(0,[-1 for _ in range(m+2)])
graph.append([-1 for _ in range(m+2)])

visited = [[False for _ in range(m+2)] for _ in range(n+2)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 처음에 1인 토마토 큐에 넣기
q = deque()
total = 0
answer = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 0:
            total += 1
        elif graph[i][j] == 1:
            deque.append(q, (0, i, j))
            visited[i][j] = True

while q:
    d, x, y = deque.popleft(q)
    answer = max(d, answer)
    for i in range(4):
        cx, cy = x + dx[i], y + dy[i]
        if graph[cx][cy] != -1 and visited[cx][cy] == False:
            deque.append(q, (d + 1, cx, cy))
            visited[cx][cy] = True
            total -= 1


if total == 0:
    print(answer)
else:
    print(-1)


