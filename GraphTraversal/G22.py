# 백준 2206번: 벽 부수고 이동하기

# 최단 경우를 구하는 문제이므로 너비우선탐색 bfs를 한다
# 이동 중에 벽을 하나 부서도 되는 것은
# 미리 모든 벽을 하나씩 제거한 상태의 그래프에서 탐색을 해서 해결한다.
# 이렇게하면 O(N*M*k) 해서 시간초과가 난다

# bfs를 수행하는데 벽을 깨고 온건지 아닌지도 저장한다.
# 방문 여부도 다르게 체크해줘야 한다.
# 큐에서 pop될때 벽을 부수고 온 것과 아닌 것은 앞으로 다르게 방문하기 때문이다.

import sys
from collections import deque

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[-1 for _ in range(m + 2)] for _ in range(n + 2)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    str = input()
    for j in range(m):
        g[i + 1][j + 1] = int(str[j])

def bfs(x, y):
    q = deque()
    deque.append(q, (1, x, y, 0))
    visited = [[[0 for _ in range(m + 2)] for _ in range(n + 2)] for _ in range(2)]
    visited[0][x][y] = 1
    visited[1][x][y] = 1
    while q:
        k, cx, cy, f = deque.popleft(q)
        if cx == n and cy == m:
            return k
        for i in range(4):
            sx, sy = cx + dx[i], cy + dy[i]
            if f == 0 and visited[0][sx][sy] == 0: # 벽을 안부신적 없고, 방문하지 않은 곳
                if g[sx][sy] == 0: # 갈 수 있는 곳
                    deque.append(q, (k + 1, sx, sy, 0))
                    visited[0][sx][sy] = 1
                    visited[1][sx][sy] = 1
                elif g[sx][sy] == 1: # 벽을 부수고 가는 곳
                    deque.append(q, (k + 1, sx, sy, 1))
                    visited[1][sx][sy] = 1
            elif f == 1 and visited[1][sx][sy] == 0 and g[sx][sy] == 0:
                deque.append(q, (k + 1, sx, sy, 1))
                visited[1][sx][sy] = 1

    return INF


answer = bfs(1, 1)
if answer == INF:
    print(-1)
else:
    print(answer)
