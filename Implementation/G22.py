# 백준 15787번: 기차가 은하수를 건너고
# 문제는 엄청 간단한 문제여서 쉽게 풀이 가능
# 문제에서 1번째 부터 시작하는데 0번째부터 배열에 넣어서
# index 오류가 생겼다
# 기본적이지만 조심
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
com = [list(map(int, input().split())) for _ in range(m)]
t = [[0 for _ in range(20)] for _ in range(n)]

for i in range(m):
    if com[i][0] == 1:
        t[com[i][1]-1][com[i][2]-1] = 1
    elif com[i][0] == 2:
        t[com[i][1]-1][com[i][2]-1] = 0
    elif com[i][0] == 3:
        t[com[i][1]-1].insert(0, 0)
        t[com[i][1]-1].pop(20)
    elif com[i][0] == 4:
        t[com[i][1]-1].insert(20, 0)
        t[com[i][1]-1].pop(0)

answer = n
for i in range(1, n):
    for j in range(0, i):
        if t[i] == t[j]:
            answer -= 1
            break
print(answer)