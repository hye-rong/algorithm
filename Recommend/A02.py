# 백준 3085번: 사탕 게임

# 바꿀 수 있는 모든 경우 확인
# 바꾼 곳에서 자기랑 같은 곳으로 얼만큼 이동할 수 있는지 확인

n = int(input())
board = [[-1 for _ in range(n + 2)]]

for i in range(n):
    str = input()
    tmp = [-1]
    for c in str:
        if c == 'C':
            tmp.append(0)
        elif c == 'P':
            tmp.append(1)
        elif c == 'Z':
            tmp.append(2)
        else:
            tmp.append(3)
    tmp.append(-1)
    board.append(tmp)
board.append([-1 for _ in range(n + 2)])


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, cnt, v):
    cx, cy = x + dx[v], y + dy[v]
    if board[cx][cy] == board[x][y]:
        return dfs(cx, cy, cnt+1, v)
    else:
        return cnt


def checkMax(ax, ay, bx, by):
    board[ax][ay], board[bx][by] = board[bx][by], board[ax][ay]
    ans = 1
    # ax, ay를 기준으로 확인
    ans = max(ans, 1+dfs(ax, ay, 0, 0) + dfs(ax, ay, 0, 1))   # 가로
    ans = max(ans, 1+dfs(ax, ay, 0, 2) + dfs(ax, ay, 0, 3))   # 세로
    # bx, by를 기준으로 확인
    ans = max(ans, 1+dfs(bx, by, 0, 0) + dfs(bx, by, 0, 1))  # 가로
    ans = max(ans, 1+dfs(bx, by, 0, 2) + dfs(bx, by, 0, 3))  # 세로
    board[ax][ay], board[bx][by] = board[bx][by], board[ax][ay]
    return ans

answer = 1
for i in range(1, n+1):
    for j in range(1, n):
        answer = max(answer, checkMax(i, j, i, j+1))
for i in range(1, n):
    for j in range(1, n+1):
        answer = max(answer, checkMax(i, j, i+1, j))
print(answer)