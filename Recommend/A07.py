# 백준 17070번: 파이프 옮기기
# 다이나믹 프로그래밍
# 가로, 세로, 대각선 방향이 모두 다르기 때문에
# 따로따로 저장
# 점화식을 세워서 계산

n = int(input())
graph = [[1 for _ in range(n+2)]]
for _ in range(n):
    graph.append([1] + list(map(int, input().split())) + [1])
graph.append([1 for _ in range(n+2)])

count = [[[0 for _ in range(n+2)] for _ in range(n+2)] for _ in range(3)]
count[0][1][2] = 1


for i in range(1, n+1):
    for j in range(3, n+1):
        if graph[i][j] == 0:
            count[0][i][j] = count[0][i][j-1] + count[2][i][j-1]
            count[1][i][j] = count[1][i-1][j] + count[2][i-1][j]
            if graph[i-1][j] == 0 and graph[i][j-1] == 0:
                count[2][i][j] = count[0][i-1][j-1] + count[1][i-1][j-1] + count[2][i-1][j-1]

answer = count[0][n][n] + count[1][n][n] + count[2][n][n]
print(answer)
