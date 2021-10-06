# 백준 1946번: 신입사원

import sys
t = int(input())
for i in range(t):
    n = int(input())
    score = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    score.sort()
    h = []
    answer = 1
    maxScore = score[0][1]
    for j in range(1, len(score)):
        if maxScore > score[j][1]:
            maxScore = score[j][1]
            answer += 1
    print(answer)

