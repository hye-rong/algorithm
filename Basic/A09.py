# 백준 1978번: 소수찾기

n = int(input())
l = list(map(int, input().split()))


def findPrime(a):
    count = 0
    if a == 1:
        return False
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
            if count > 2:
                return False
    return True

answer = 0
for i in l:
    if findPrime(i):
        answer += 1

print(answer)