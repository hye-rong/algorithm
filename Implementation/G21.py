# 백준 16926번: 배열 돌리기 1
# 이 문제도 역시 rotate를 r번 해서 해결하기도 한다
# 돌려야 되는 for문이 min(n, m)/2 라는 것을 알면 쉽게 해결된다.
# 큐를 사용해서 숫자를 돌리면서 동시에 읽고
# 써야하는 순간이 오면 pop해서 쓰는 방식으로 하면
# 3번 사용한 for문을 줄일 수 있다.
# 배열은 인덱스 계산과, 저장을 조심하는 것이 중요하다.
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


answer = [[0 for _ in range(m)] for _ in range(n)]
tmp = [[] for _ in range(min(n, m)//2)]
for i in range(min(n, m)//2): # 한 줄씩 미리 담아두기
    a, b = i, i
    d = 0 # 방향
    while True:
        a, b = a + dx[d], b + dy[d]
        if a < i or a >= (n - i) or b < i or b >= (m - i): # 범위를 나간 경우
            a, b = a - dx[d], b - dy[d]
            d = d + 1
            if d > 3:
                break
            a, b = a + dx[d], b + dy[d]
        tmp[i].append(g[a][b])


for i in range(min(n, m)//2): # 어떤 좌표를 시작점으로 하는지
    a, b = i, i
    d = 0 # 방향
    dr = r % ((n+m-2-4*i)*2)
    for k in range(dr):
        a, b = a + dx[d], b + dy[d]
        if a < i or a >= (n - i) or b < i or b >= (m - i): # 범위를 나간 경우
            a, b = a - dx[d], b - dy[d]
            d = (d + 1) % 4
            a, b = a + dx[d], b + dy[d]
        tmp[i].append(g[a][b])
    # 넣어주는 작업
    for k in tmp[i]:
        a, b = a + dx[d], b + dy[d]
        if a < i or a >= (n - i) or b < i or b >= (m - i): # 범위를 나간 경우
            a, b = a - dx[d], b - dy[d]
            d = (d + 1) % 4
            a, b = a + dx[d], b + dy[d]
        answer[a][b] = k

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()