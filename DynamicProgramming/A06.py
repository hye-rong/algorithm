# 프로그래머스 동적계획법 도둑질

def solution(money):
    answer = 0
    dp = [[0 for _ in range(len(money))] for _ in range(2)]
    dp[0][0] = money[0]

    for i in range(1, len(money)):
        dp[0][i] = dp[1][i - 1] + money[i]
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1])
    # 마지막 집이 안털린 경우가 더 크면 return
    if dp[1][-1] > dp[0][-1]:
        return dp[1][-1]
    # 마지막 집이 턴 경우가 더 크면 첫 번째 집을 털지 않은 경우와 비교해줘야 함
    dp2 = [[0 for _ in range(len(money) - 1)] for _ in range(2)]
    dp2[0][0] = money[1]

    for i in range(2, len(money)):
        dp2[0][i - 1] = dp2[1][i - 2] + money[i]
        dp2[1][i - 1] = max(dp2[0][i - 2], dp2[1][i - 2])

    return max(dp2[0][-1], dp2[1][-1], dp[1][-1])