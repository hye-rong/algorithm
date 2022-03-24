# 백준 16953번: A -> B

from collections import deque

a, b = map(int, input().split())

def bfs(x, y):
    q = deque()
    q.append((x, 0))
    while q:
        num, cnt = q.popleft()
        if num == y:
            return cnt + 1
        elif num < y:
            q.append((num*2, cnt+1))
            q.append((num*10+1, cnt+1))

    return -1

print(bfs(a, b))