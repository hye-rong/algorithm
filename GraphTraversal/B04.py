# 백준 12851번: 숨바꼭질 2
# 가장 빠른 시간을 찾기 때문에 bfs를 이용
# 한 위치에 오는 여러 경우의 수가 있을 때
# 따로 센다면, 그 뒤의 경우는 그 경우의 수만큼 곱해져서 경우가 늘어남
# 그 지점까지 오는 최소의 경로의 경우의 수를 저장
# 큐에 넣을 때, cnt가 작은 순서대로 들어가기 때문에 문제 없음

from collections import deque

n, k = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]
visited[n] = [0, 1]


def bfs(n):
    q = deque()
    q.append(n)

    while q:
        a = q.popleft()
        for i in [a+1, a-1, a*2]:
            if 0 <= i <= 100000:
                if visited[i][0] == -1:
                    q.append(i)
                    visited[i][0] = visited[a][0]+1
                    visited[i][1] = visited[a][1]
                elif visited[i][0] == visited[a][0]+1:
                    visited[i][1] += visited[a][1]


bfs(n)
print(visited[k][0])
print(visited[k][1])