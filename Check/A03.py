# 백준 14719번: 빗물

h, w = map(int, input().split())
block = map(int, input().split())

answer = 0
cur = block[0]
start = 1
for i in range(1, w):
    if block[i] == 0:

    if block[i] >= cur:
        for j in range(start, i):
