from collections import deque
n, k = map(int, input().split())
vmap = [[-1 for _ in range(n+2)] for _ in range(n+2)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n+1):
    vmap[i][1:-1] = list(map(int, input().split()))
s, x, y = map(int, input().split())

deq = deque()
deq.append((x, y, 0))

check = k + 1
fin_time = s
while deq:
    cx, cy, time = deq.popleft()
    if time > fin_time:
        break
    if vmap[cx][cy] != 0:
        fin_time = time
        check = min(check, vmap[cx][cy])
    else:
        for i in range(4):
            if vmap[cx+dx[i]][cy+dy[i]]!=-1:
                deq.append((cx+dx[i], cy+dy[i], time+1))
if check == k+1:
    print(0)
else:
    print(check)