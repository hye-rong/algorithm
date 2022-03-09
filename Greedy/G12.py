# 백준 20365번 : 블로그 2
# 붙어 있는 색은 하나의 색으로 봐도 된다.
# 그렇게 중복을 제거해서 개수를 세면 서로 색이 바뀌는 개수를 구할 수 있다
# 짝수면 아무 색이나 먼저 칠하면 되고,
# 홀수면 더 많은 색을 먼저 칠하면 된다.
# 그러면 결국 2로 나눈 몫과 전체 칠하는 1번을 더하면 답이 된다.
import sys

input = sys.stdin.readline
n = int(input())
s = input()
answer = 0
cur = ''
for i in range(n):
    if cur != s[i]:
        cur = s[i]
        answer += 1
print(answer//2 + 1)