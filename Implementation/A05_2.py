# 프로그래머스: 기둥과 보 설치
# 해결책: 2차원 배열에 해당 위치에 맞게 저장을 해서 search시간이 줄어즘
# 개선: remove할 때, is_okay함수 이용
def solution(n, build_frame):
    answer = []
    array_build = [[[0 for i in range(n + 3)] for j in range(n + 3)] for k in range(2)]

    for build in build_frame:
        if build[3] == 0:  # 삭제
            array_build[build[2]][build[0] + 1][build[1] + 1] = 0
            if not remove_okay(build, array_build):
                array_build[build[2]][build[0] + 1][build[1] + 1] = 1
        else:  # 설치
            if is_okay(build, array_build):
                array_build[build[2]][build[0] + 1][build[1] + 1] = 1

    for i in range(n + 3):
        for j in range(n + 3):
            for k in range(2):
                if array_build[k][i][j]:
                    answer.append([i - 1, j - 1, k])

    return answer


def is_okay(build, array_build):
    x, y, a, b = build
    x += 1
    y += 1
    if a == 0:  # 기둥
        if y == 1 or array_build[1][x][y] or array_build[1][x - 1][y] or array_build[0][x][y - 1]:
            return True
        return False
    else:  # 보
        if array_build[0][x][y - 1] or array_build[0][x + 1][y - 1]:
            return True
        if array_build[1][x - 1][y] and array_build[1][x + 1][y]:
            return True
        return False


def remove_okay(build, array_build):
    x, y, a, b = build
    if a == 0:  # 기둥
        if array_build[0][x + 1][y + 2] and not is_okay([x, y + 1, 0, 0], array_build):
            return False
        if array_build[1][x][y + 2] and not is_okay([x - 1, y + 1, 1, 0], array_build):
            return False
        if array_build[1][x + 1][y + 2] and not is_okay([x, y + 1, 1, 0], array_build):
            return False
    else:  # 보
        if array_build[1][x][y + 1] and not is_okay([x - 1, y, 1, 0], array_build):
            return False
        if array_build[0][x + 1][y + 1] and not is_okay([x, y, 0, 0], array_build):
            return False
        if array_build[0][x + 2][y + 1] and not is_okay([x + 1, y, 0, 0], array_build):
            return False
        if array_build[1][x + 2][y + 1] and not is_okay([x + 1, y, 1, 0], array_build):
            return False
    return True