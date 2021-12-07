# 프로그래머스: (그래프) 가장 먼 노드

# 다익스트라 (1번 노드에서 각 노드까지의 최소 경로 구하기) -> 시간 초과
# BFS (1번 노드에서 bfs 수행)

import heapq


def solution(n, edge):
    answer = 0
    INF = int(1e9)
    edgeInNode = [[] for _ in range(n + 1)]  # 각 노드에서 갈 수 있는 노드들 저장
    check = [False] * (n + 1)  # 노드 방문 여부
    for e in edge:
        edgeInNode[e[0]].append(e[1])
        edgeInNode[e[1]].append(e[0])
    # BFS
    q = []
    heapq.heappush(q, [0, 1])  # count, node number
    maxDist = 0
    while q:
        dist, num = heapq.heappop(q)
        if check[num]:
            continue
        check[num] = True
        if dist > maxDist:
            maxDist = dist
            answer = 1
        else:
            answer += 1
        for e in edgeInNode[num]:
            heapq.heappush(q, [dist + 1, e])

    return answer