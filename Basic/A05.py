# 10870번: 피보나치 수

def findFibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return findFibo(n-1) + findFibo(n-2)

n = int(input())
print(findFibo(n))