# 백준 11399번: ATM
import sys

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
m.sort()

answer = 0
for i in range(n):
    answer += m[i]*(n-i)

print(answer)