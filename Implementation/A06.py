from itertools import combinations

n, m = map(int, input().split())

list_home = []
list_chicken = []
dists = []

for i in range(n):
    mlist = input().split()
    for j in range(n):
        if mlist[j] == '0':
            pass
        elif mlist[j] == '1':
            list_home.append((i + 1, j + 1))
        else:
            list_chicken.append((i + 1, j + 1))

for chicken in list_chicken:
    tmp = []
    for home in list_home:
        tmp.append(abs(chicken[0] - home[0]) + abs(chicken[1] - home[1]))
    dists.append(tmp)

datas = combinations(dists, m)

sum_result = []
for data in datas:
    sum_dist = 0
    for i in range(len(list_home)):
        tmp = []
        for j in range(m):
            tmp.append(data[j][i])
        sum_dist += min(tmp)
    sum_result.append(sum_dist)
print(min(sum_result))