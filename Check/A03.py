# 백준 14719번: 빗물

# 맨 위부터 시작해서
# 2개 이상이면 그 사이에 고이도록 한다

h, w = map(int, input().split())
block = list(map(int, input().split()))
graph = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if block[j] >= h - i:
            graph[i][j] = 1

answer = 0
tmp = 0
flag = False
for i in range(h):
    flag = False
    tmp = 0
    for j in range(w):
        if graph[i][j] == 1:
            if flag:
                answer += tmp
                tmp = 0
            else:
                flag = True
        else:
            if flag:
                tmp += 1
print(answer)
