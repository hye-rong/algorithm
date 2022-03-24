# 백준 13549번: 숨바꼭질 3
# 가장 빠른 시간을 구하기 때문에 bfs
# 모든 경우를 다 구하는 것이기 때문에
# 경우에 따라 count가 다르지만 우선 순위 큐를 사용하지 않음

from collections import deque

n, k = map(int, input().split())
visited = [-1 for _ in range(100001)]
visited[n] = 0


def bfs(n):
    q = deque()
    q.append(n)

    while q:
        a = q.popleft()
        for i in [a+1, a-1]:
            if 0 <= i <= 100000:
                if visited[i] == -1:
                    q.append(i)
                    visited[i] = visited[a] + 1
                elif visited[i] > visited[a]+1:
                    q.append(i)
                    visited[i] = visited[a] + 1
        b = a*2
        if 0 <= b <= 100000:
            if visited[b] == -1:
                q.append(b)
                visited[b] = visited[a]
            elif visited[b] > visited[a]:
                q.append(b)
                visited[b] = visited[a]


bfs(n)
print(visited[k])