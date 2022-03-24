# 백준 1789번: 수들의 합

# n개의 최댓값이므로 최대한 작은 자연수는 포함시켜야함

s = int(input())

sum = 0
num = 0
while sum < s:
    num += 1
    sum += num
    print(num, sum)
if sum == s:
    print(num)
else:
    print(num-1)