# 백준 14226번: 이모티콘
# 최솟값을 구하는 프로그램이므로 bfs 사용
from collections import deque

s = int(input())
visited = [0 for _ in range(1001)]

def dfs(s):
    q = deque()
    q.append((1, 0, 0)) # 1개, 클립보드 0개
    while q:
        a, copy, cnt = q.popleft()
        if a == s:
            print(cnt)
            break
        if 0 <= a <= 1000 and visited[a] == 0:
            q.append((a, a, cnt+1))
            q.append((a-1, copy, cnt+1))
            visited[a] = 1
        if copy != 0:
            q.append((a+copy, copy, cnt+1))

dfs(s)