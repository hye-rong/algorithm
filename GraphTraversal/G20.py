# 백준 16954번: 움직이는 미로 탈출
# 벽을 만나게 되면 실패
# dfs를 수행해서 가능한 경우가 있는지 전체 탐색을 해야한다
# 벽은 제일 아래로 가면 사라지기 때문에 8턴 안에 벽을 만나지 않으면 성공

# 미리 8개의 벽 만들어 두기

wall = [[[-1 for _ in range(10)] for _ in range(10)] for _ in range(8)]

dx = [0, -1, 0, 1, -1, -1, 1, 1, 0]
dy = [-1, 0, 1, 0, -1, 1, 1, -1, 0]

for i in range(8):
    g = input()
    for j in range(8):
        if g[j] == "#":
            wall[0][i + 1][j + 1] = 1
        else:
            wall[0][i + 1][j + 1] = 0

for k in range(1, 8):
    for i in range(2, 9):
        for j in range(1, 9):
            wall[k][i][j] = wall[k - 1][i - 1][j]
    for i in range(1, 9):
        wall[k][1][i] = 0


def dfs(k, x, y):
    if k == 7:
        return True
    flag = False
    for i in range(9):
        if flag:
            break
        cx, cy = x + dx[i], y + dy[i]
        if wall[k][cx][cy] == 0:  # 벽이 아니면 이동
            if wall[k + 1][cx][cy] == 0:  # 벽을 이동시켜서 만나는지 확인
                if dfs(k + 1, cx, cy):
                    flag = True
    return flag


if dfs(0, 8, 1):
    print(1)
else:
    print(0)
