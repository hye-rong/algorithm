# 백준 1292번: 쉽게 푸는 문제

def findNumber(a):
    cur = 1
    while True:
        a -= cur
        if a <= 0:
            return a, cur
        cur += 1


a, b = map(int, input().split())
a, x = findNumber(a)
b, y = findNumber(b)

answer = 0
if x != y:
    answer += x * (1 - a)
    answer += y * (y + b)
    if x + 1 < y:
        for i in range(x+1, y):
            answer += i*i
else:
    answer = (b-a+1)*x
print(answer)
