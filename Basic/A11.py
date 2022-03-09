# 백준 2581번: 소수
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

m = int(input())
n = int(input())


sum = 0
minNum = 0
for i in range(m, n+1):
    if findPrime(i):
        sum += i
        if minNum == 0:
            minNum = i
if sum == 0:
    print(-1)
else:
    print(sum)
    print(minNum)
