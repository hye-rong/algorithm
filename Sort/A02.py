# 백준 18310번: 안테나

import sys

n = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
dist.sort()

print(dist[(n-1) // 2])


