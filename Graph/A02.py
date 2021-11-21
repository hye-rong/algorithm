# 백준 3665번: 최종 순위
import sys
from collections import deque

def topology_sort():
    # 토폴로지 소트
    # 들어오는 edge 개수 세기
    result = []
    indegree = [0] * (n + 1)
    for edge in edges:
        for i in edge:
            indegree[i] += 1

    q = deque()

    # 들어오는 edge가 0인 노드 큐에 넣기
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        if len(q) != 1:
            print("?")
            return
        now = q.popleft()
        result.append(now)
        for i in edges[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) == n:
        for i in result:
            print(i, end=' ')
    else:
        print("IMPOSSIBLE")

input = sys.stdin.readline

testNum = int(input())

for _ in range(testNum):
    n = int(input())
    score = list(map(int, input().split()))
    m = int(input())
    if m == 0:
        for i in score:
            print(i, end=' ')
        continue

    rank = sorted(range(1, len(score) + 1), key=lambda x: score[x - 1]) # 팀 별 등수 저장
    changes = [list(map(int, input().split())) for _ in range(m)]
    edges = [[] for _ in range(n + 1)] # 노드 별 이동 가능

    for i in range(n - 1):
        edges[score[i]] = score[i + 1:]

    for change in changes:
        a, b = change
        if rank[a - 1] < rank[b - 1]:  # 원래 a가 등수 높음
            edges[a].remove(b)
            edges[b].append(a)
        else:
            edges[b].remove(a)
            edges[a].append(b)


    topology_sort()





