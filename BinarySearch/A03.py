# 백준 2110번: 공유기 설치
import sys

n, c = map(int, sys.stdin.readline().split())
loc = [int(sys.stdin.readline()) for _ in range(n)]
loc.sort()
start = 1
end = loc[-1] - loc[0]

while start <= end:
    mid = (start + end)//2
    before = loc[0]
    count = 1
    for i in range(1, len(loc)):
        if loc[i] - before < mid:
            continue
        else:
            count += 1
            before = loc[i]
            if count >= c:
                start = mid + 1
                break
    else:
        end = mid - 1
print(end)
