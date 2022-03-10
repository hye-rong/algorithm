# 백준 14888번: 연산자 끼워넣기
# 전체 탐색?
# 순열을 이용해서 전체 탐색을 하면 미리 계산한 값을 또 계산하는 상황 발생
# 해결을 위해서는 dfs를 이용해서 탐색을 해서 기존 계산 값을 이용

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maxNum = -1e9
minNum = 1e9


def dfs(cur, i, a, b, c, d):
    global maxNum, minNum  # 전역 변수를 특정 함수로
    if i == n:
        maxNum = max(cur, maxNum)
        minNum = min(minNum, cur)
    else:
        if a > 0:
            dfs(cur + num[i], i + 1, a - 1, b, c, d)
        if b > 0:
            dfs(cur - num[i], i + 1, a, b - 1, c, d)
        if c > 0:
            dfs(cur * num[i], i + 1, a, b, c - 1, d)
        if d > 0:
            if cur < 0 and num[i] > 0:
                dfs(-(-cur // num[i]), i + 1, a, b, c, d - 1)
            else:
                dfs(cur // num[i], i + 1, a, b, c, d - 1)


dfs(num[0], 1, op[0], op[1], op[2], op[3])
print(maxNum)
print(minNum)
