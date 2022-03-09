# 백준 2609번: 최대공약수와 최소공배수

def findCommonDivisor(a, b):
    l = []
    cur = 1
    for i in range(a):
        if a % cur == 0 and b % cur == 0:
            l.append(cur)
        cur += 1
    return max(l)

def findCommonMultiple(a, b, d):
    x, y = a//d, b//d
    return x*y*d



n, m = map(int, input().split())
cd = findCommonDivisor(n, m)
cm = findCommonMultiple(n, m, cd)

print(cd)
print(cm)