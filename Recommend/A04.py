# 백준 2294번: 동전 2
# 동전 1과 같은 방식
# 안되는 경우를 0으로 설정하면 min에서 문제가 있어서 k+1로 설정

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [k+1] * (k+1)
dp[0] = 0
for i in coins:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i]+1)

if dp[-1] == k+1:
    print(-1)
else:
    print(dp[-1])