# 백준 12845번: 모두의 마블

# 10 30 20 40
n = int(input())
numbers = list(map(int, input().split()))
print(sum(numbers) + max(numbers)*(n-2))