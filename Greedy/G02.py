# 백준 2217번: 로프
# Greedy 문제
import sys

input = sys.stdin.readline

n = int(input())
w = []
for i in range(n):
    w.append(int(input()))
w.sort()

answer = 0
for i in range(n):
    answer = max(answer, w[i]*(n-i))

print(answer)