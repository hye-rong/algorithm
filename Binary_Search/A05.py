# 백준 3079번: 입국심사
import sys
n, m = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]

start = 1
end = min(a) * m

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in a:
        count += mid // i
    if count < m:
        start = mid + 1
    else:
        end = mid - 1
print(start)