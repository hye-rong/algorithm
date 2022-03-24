# 백준 16930번: 달리기
# 너비 우선 탐색
# 시간을 위해서 양쪽에서 bfs 수행했더니 더 오래걸림..
# bfs를 수행하면서 break를 할 수 있는 부분을 찾는것이 핵심

from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[-1 for _ in range(m + 2)]]
for i in range(n):
    str = input()
    tmp = [-1]
    for j in range(m):
        if str[j] == '.':
            tmp.append(0)
        elif str[j] == '#':
            tmp.append(-1)
    tmp.append(-1)
    graph.append(tmp)
graph.append([-1 for _ in range(m + 2)])

point = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x1, y1, x2, y2):
    q1 = deque()
    q1.append([x1, y1, 0])
    graph[x1][y1] = -1

    while q1:
        a, b, c = q1.popleft()
        if a == x2 and b == y2:
            return c
        for i in range(4):
            for j in range(1, k + 1):
                cx, cy = a + dx[i] * j, b + dy[i] * j
                if graph[cx][cy] == -1:  # 벽 만남
                    break
                if graph[cx][cy] == 0:
                    graph[cx][cy] = c + 1
                    q1.append([cx, cy, c + 1])
                else:
                    if graph[cx][cy] <= c:
                        break

    return -1


print(bfs(point[0], point[1], point[2], point[3]))
