# 프로그래머스 그래프 > 순위
def solution(n, results):
    answer = 0
    graph = [[False] * n for _ in range(n)]

    # 플로이드 워셜 알고리즘 이용
    # 다른 곳으로 가는 길이 하나라도 있으면 성공

    for result in results:
        a, b = result
        graph[a - 1][b - 1] = True

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    for i in range(n):
        count = 0
        for j in range(n):
            if graph[i][j] or graph[j][i]:
                count += 1
        if count == n - 1:
            answer += 1
    return answer
