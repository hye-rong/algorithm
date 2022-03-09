# 백준 21608번: 상어 초등학교

# 주어진 조건에 맞게 코드를 작성하면 되는 문제
# 조건만 맞추면 비교적 간단한 문제

import sys

def findNoLike(): # 좋아하는 학생이 없는 경우에 빈 인접한 칸이 가장 많은 곳 -> 시간 줄이려면 써도 되는데 안씀
    maxSpace = -1 # 빈칸의 개수
    a,b = 0, 0
    for i in range(1, n+2):
        for j in range(1, n+2):
            space = 0
            if graph[i][j] != 0:
                continue
            for k in range(4):
                if graph[i+dx[k]][j+dy[k]] == 0:
                    space += 1
            if space == 4:
                return (i, j)
            if space > maxSpace:
                maxSpace = space
                a, b = i, j
    return (a, b)

def findLike(x,y,z,q): # 좋아하는 학생 근처 자리 찾기
    maxSpace = -1 # 인접한 곳 중 빈칸
    maxLike = -1 # 인접한 곳 중 좋아하는 학생
    a, b = 0, 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            space = 0
            like = 0
            if graph[i][j] != 0:
                continue
            for k in range(4):
                cur = graph[i+dx[k]][j+dy[k]]
                if cur==x or cur==y or cur==z or cur==q:
                    like += 1
                if cur == 0:
                    space += 1
            if like > maxLike:
                maxSpace = space
                maxLike = like
                a, b = i, j
            elif like == maxLike:
                if space > maxSpace:
                    maxSpace = space
                    a,b = i, j
    return (a, b)

input = sys.stdin.readline
n = int(input())
likeNum = [list(map(int, input().split())) for _ in range(n*n)]
graph = [[-1 for _ in range(n+2)]]
for _ in range(n):
    graph.append([-1] + [0 for _ in range(n)] + [-1])
graph.append([-1 for _ in range(n+2)])

check = []
loc = []
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for i in likeNum:
    check.append(i[0])
    count = 0
    for j in range(1, 5):
        if i[j] in check:
            count += 1
    if count == 0:
        a, b = findLike(i[1],i[2],i[3],i[4])
        graph[a][b] = i[0]
        loc.append([a,b])
    else:
        a,b = findLike(i[1],i[2],i[3],i[4])
        graph[a][b] = i[0]
        loc.append([a, b])

# 만족도 확인
answer = 0
plus = [0, 1, 10, 100, 1000]
for i in range(n*n):
    _, x, y, z, q = likeNum[i]
    a, b = loc[i]
    count = 0
    for k in range(4):
        cur = graph[a+dx[k]][b+dy[k]]
        if cur==x or cur==y or cur==z or cur==q:
            count += 1
    answer += plus[count]

print(answer)
