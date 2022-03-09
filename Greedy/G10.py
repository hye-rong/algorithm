# 백준 1931번: 회의실 배정
# 끝나는 시간을 기준으로 정렬
# 끝나는 시간이 제일 빠른 것부터 시작
# -> 얘는 무조건 정답에 들어갈 수 있다
# -> 이것을 선택안해야 선택할 수 있는 회의가 있다고 해도
# -> 그 선택보다 이 선택이 더 먼저 끝나니까 더 좋은 선택이다
# "현재를 기준으로 종료시간이 빨라야 더 많은 회의 가능"
# 정렬된 순서대로 들어갈 수 있는 회의를 다 채워서 넣는다
# 한번 틀린 이유: 회의 시작과 회의 끝이 같을 수 있는데
# 정렬할 때 끝나는 시간이 같은 경우, 시작 시간이 작은 순으로 해야지
# 끝나는 시간이 같은 회의가 있을 때, 두 경우를 모두 세어줄 수 있다
import sys

input = sys.stdin.readline
t = []
n = int(input())
for i in range(n):
    t.append(list(map(int, input().split())))
t.sort(key = lambda x:(x[1], x[0])) # 끝나는 시간이 빠른 순서대로 정렬
answer = 0
end = 0
for i in t:
    if i[0] >= end:
        end = i[1]
        answer += 1
print(answer)