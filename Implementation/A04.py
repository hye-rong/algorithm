N = int(input())
board = [[0 for i in range(N)] for j in range(N)]
board[0][0] = 1
K = int(input())
for i in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2
num = int(input())
turns = []
for i in range(num):
    n, d = input().split()
    turns.append([int(n), d])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
way = 0
answer = 0
loc = [0, 0]
snake = [[0, 0]]
while True:
    answer += 1
    nx = loc[0] + dx[way]
    ny = loc[1] + dy[way]
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1:
        print(answer)
        break
    elif board[nx][ny] == 0:
        px, py = snake.pop(0)
        board[px][py] = 0
    board[nx][ny] = 1
    snake.append([nx, ny])
    loc = [nx, ny]
    if len(turns) != 0 and answer == turns[0][0]:
        if turns[0][1] == 'L':
            way += 3
        else:
            way += 1
        way = way % 4
        turns.pop(0)