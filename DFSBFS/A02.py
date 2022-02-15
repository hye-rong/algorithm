import itertools
from collections import deque
n, m = map(int, input().split())
zero_set = set()
virus = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 0:
            zero_set.add((i, j))
        elif tmp[j] == 2:
            virus.append((i, j))
datas = itertools.combinations(zero_set, 3)

answer = 0

# 조합으로 벽을 세울 곳 data에 저장
for data in datas:
    cur_set = zero_set.copy()
    for x, y in data:
        cur_set.remove((x,y))
    deq = deque()
    for x, y in virus:
        for i in range(4):
            if (x+dx[i], y+dy[i]) in cur_set:
                deq.append((x+dx[i], y+dy[i]))
    while deq:
        a, b = deq.popleft()
        if (a,b) in cur_set:
            cur_set.remove((a, b))
            if len(cur_set)<answer:
                break
            for i in range(4):
                if (a+dx[i], b+dy[i]) in cur_set:
                    deq.append((a+dx[i], b+dy[i]))
    answer = max(len(cur_set), answer)

print(answer)