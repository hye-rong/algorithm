# 프로그래머스 동적계획법 정수삼각형

def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][0] += triangle[i-1][0]
            elif j == i:
                triangle[i][i] += triangle[i-1][i-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    answer = max(triangle[-1])
    return answer