import sys
import copy

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[0] * 4 for _ in range(4)]  # 물고기 번호
arrow = [[0] * 4 for _ in range(4)]  # 물고기 방향
location = [[0, 0] for _ in range(17)]  # 물고기 위치

for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(4):
        graph[i][j] = tmp[j * 2]
        location[tmp[j * 2]][0], location[tmp[j * 2]][1] = i, j
        arrow[i][j] = tmp[j * 2 + 1] - 1  # 방향 0부터 설정

count = graph[0][0]
location[graph[0][0]][0] = -1
location[0][0], location[0][1] = 0, 0
graph[0][0] = -1


def print_graph(g):
    for i in range(4):
        for j in range(4):
            if g[i][j] == -1:
                print("상", end=' ')
            elif g[i][j] == 0:
                print("X", end=' ')
            else:
                print(g[i][j], end=' ')
        print()


# 번호 작은 물고기부터 이동
# 찾는 방법 1) 배열에서 하나씩 다 찾음 2)미리 순서별로 위치 저장해둠 -> 2번으로 함

def move_fish(graph, arrow, location, count):

    for i in range(1, 17):  # 물고기 순서대로 이동
        x, y = location[i]
        if x == -1:  # 물고기 없는 경우
            continue
        for _ in range(8):  # 방향 돌리기
            a = arrow[x][y]
            cx, cy = x + dx[a], y + dy[a]
            if 0 <= cx < 4 and 0 <= cy < 4 and graph[cx][cy] >= 0:  # 범위 내에 있고 물고기인 경우
                print("자리바꿈{0}<->{1}".format(graph[x][y], graph[cx][cy]))
                # 위치 변경
                location[graph[x][y]][0], location[graph[x][y]][1] = cx, cy
                if graph[cx][cy] != 0:
                    location[graph[cx][cy]][0], location[graph[cx][cy]][1] = x, y
                graph[x][y], graph[cx][cy] = graph[cx][cy], graph[x][y]
                arrow[x][y], arrow[cx][cy] = arrow[cx][cy], arrow[x][y]
                break
            else:  # 방향 바꿔야 하는 경우
                arrow[x][y] = (arrow[x][y] + 1) % 8

    print("----move_fish----")
    print_graph(graph)
    return move_shark(graph, arrow, location, count)


def move_shark(graph, arrow, location, count):
    # 상어가 이동할 수 있는 곳 찾음
    x, y = location[0]
    maxSum = count
    for i in range(1, 4):
        cx, cy = x + dx[arrow[x][y]] * i, y + dy[arrow[x][y]] * i
        if 0 <= cx < 4 and 0 <= cy < 4 and graph[cx][cy] > 0:  # 이동 가능
            # 이동 시키기
            cgraph = copy.deepcopy(graph)
            carrow = copy.deepcopy(arrow)
            clocation = copy.deepcopy(location)

            clocation[0][0], clocation[0][1] = cx, cy # 상어 위치 갱신

            clocation[cgraph[cx][cy]][0], clocation[cgraph[cx][cy]][1] = -1, -1 # 먹힌 물고기 -1 로 설정
            carrow[x][y] = carrow[cx][cy]
            tmp = cgraph[cx][cy] + count
            cgraph[cx][cy] = -1
            cgraph[x][y] = 0
            #print("-----count:", count)
            maxSum = max(maxSum, move_fish(cgraph, carrow, clocation, tmp))
    #print("maxSum", maxSum)
    return maxSum


answer=move_fish(graph, arrow, location, count)
print(answer)
