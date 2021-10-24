# 백준 1654번: 랜선 자르기
import sys

k, n = map(int, sys.stdin.readline().split())
line = [int(sys.stdin.readline()) for _ in range(k)]
start = 1
end = max(line)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for num in line:
        count += num // mid
    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)




