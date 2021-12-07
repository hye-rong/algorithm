# 백준 2875번: 대회 or 인턴

# 여학생 2명 남학생 1명
import math
n, m, k = map(int, input().split())
answer = min(n//2, m)
k = k - (n + m - 3*answer)

if k > 0:
    answer -= math.ceil(k/3)
print(answer)