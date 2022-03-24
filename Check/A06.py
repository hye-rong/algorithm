# 백준 1806번: 부분합
# 투포인터 문제

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
a = 0
b = 0
answer = n+1
sum = numbers[0]
while b < n:
    if sum >= s: # 부분합이 되는 경우
        answer = min(answer, b-a+1)
        sum -= numbers[a]
        a += 1
    else:
        b += 1
        if b == n:
            break
        else:
            sum += numbers[b]
if answer == n+1:
    print(0)
else:
    print(answer)
