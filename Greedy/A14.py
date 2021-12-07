# 백준 1744번: 수 묶기
import sys
input = sys.stdin.readline
n = int(input())
plus = [1]
minus = [1]
answer = 0
for i in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num == 1:
        answer += 1
    else:
        minus.append(num)
plus.sort(reverse=True)
minus.sort()
for i in range(len(plus)//2):
    answer += plus[i*2]*plus[i*2+1]
for i in range(len(minus)//2):
    answer += minus[i*2]*minus[i*2+1]

print(answer)