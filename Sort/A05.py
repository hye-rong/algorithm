# 백준 10816번: 숫자 카드2

n = int(input())
cards = list(map(int, input().split()))
dic = {}
for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
m = int(input())
checks = list(map(int, input().split()))
answer = []
for i in checks:
    if i in dic:
        answer.append(str(dic[i]))
    else:
        answer.append('0')
print(' '.join(answer))
