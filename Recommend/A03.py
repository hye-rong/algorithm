# 백준 2293번: 동전
# 다이나믹 프로그래밍 문제
# 이전 저장된 것을 사용할 때, 동전만큼 뒤로 이동

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

count_list = [0] * (k + 1)
# x원짜리 동전 하나로 x원을 만드는 경우의 수 = 1
count_list[0] = 1 # 0원

for i in coin:
    for j in range(i, k + 1):
        count_list[j] += count_list[j - i]

print(count_list[k])