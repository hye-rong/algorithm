# 백준 14501번: 퇴사

n = int(input())
days = [0 for _ in range(n+1)]
works = []
for i in range(n):
    a, b = map(int, input().split())
    if a + i <= n:
        works.append([a + i, i, b])
works.sort()

cur = 0
for w in works:
    end, start, money = w
    if end == cur:
        days[end] = max(days[end], days[start] + money)
    else:
        for i in range(cur+1, end):
            days[i] = days[cur]
        days[end] = max(days[start] + money, days[end-1])
        cur = end
print(max(days))

