# 백준 16236번: 아기 상어
import sys
from collections import deque

input = sys.stdin.readline

# 상어 위치에서 bfs수행해서 가장 가까운 먹이 찾음
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(level, cx, cy):
    check = [[0] * n for _ in range(n)]
    q = deque()
    q.append([cx, cy, 0])  # x, y, 이동거리
    check[cx][cy] = 1

    while q:
        px, py, pc = q.popleft()
        if 0 < graph[px][py] < level:
            # 지금 큐에 있는 애들 중 count, x, y 순으로 오름차순 sort
            q.append([px, py, pc])
            fin = sorted(q, key=lambda x: (x[2], x[0], x[1]))   # count, x, y 순으로 sort
            for data in fin:
                if 0 < graph[data[0]][data[1]] < level:
                    return data
        for i in range(4):
            cx = px + dx[i]
            cy = py + dy[i]
            if 0 <= cx < n and 0 <= cy < n and check[cx][cy] == 0:
                if graph[cx][cy] <= level:
                    q.append([cx, cy, pc + 1])
                    check[cx][cy] = 1

    return 0, 0, 0


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

level = 2
level_count = 2
result = 0
cx, cy = 0, 0
# 상어의 현재 위치 구하기 -> index 쓰려면 있는지 또 확인해야해서 그냥 찾아줌
flag = False
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            cx, cy = i, j
            flag = True
            break
    if flag:
        break

while True:
    cx, cy, count = bfs(level, cx, cy)
    if count == 0:  # 먹을 수 있는 것이 없음
        break
    graph[cx][cy] = 0
    result += count
    level_count -= 1
    if level_count == 0:
        level += 1
        level_count = level

    print("물고기 레벨{0} -> 현재 위치:{1},{2}  움직인 거리:{3}  레벨업까지 남은 물고기:{4}".format(level, cx,cy,result,level_count))

print(result)
