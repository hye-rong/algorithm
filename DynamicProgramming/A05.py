# 프로그래머스 동적계획법 등굣길

def solution(m, n, puddles):
    answer = 0
    cmap = [[0 for _ in range(m+1)] for _ in range(n+1)]
    cmap[0][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if not [j, i] in puddles:
                cmap[i][j] = cmap[i][j-1] + cmap[i-1][j]
    return cmap[-1][-1]%1000000007