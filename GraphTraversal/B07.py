# 백준 13913번: 숨바꼭질 4
from collections import deque

n, k = map(int, input().split())

visited = [-1 for _ in range(100001)]
visited[n] = n

def bfs(n, k):
    q = deque()
    q.append((n, 0))
    while q:
        a, cnt = q.popleft()
        if a == k:
            print(cnt)
            result = [k]
            while True:
                if result[-1] == n:
                    break
                x = visited[result[-1]]
                result.append(x)

            for j in range(len(result)):
                print(result[len(result)-j-1], end=' ')
            break
        for i in [a+1, a-1, a*2]:
            if 0 <= i <= 100000:
                if visited[i] == -1:
                    visited[i] = a
                    q.append((i, cnt+1))

bfs(n, k)