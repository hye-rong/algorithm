# 백준 2460번: 지능형 기차

l = []
for i in range(10):
    l.append(list(map(int, input().split())))

answer = 0
p = 0
for i in l:
    a, b = i
    p -= a
    answer = max(p, answer)
    p += b
    answer = max(p, answer)
print(answer)