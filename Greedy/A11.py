# 백준 1541번 잃어버린 괄호
import sys

str = input()
divideList = str.split('-')
answer = sum(list(map(int, divideList[0].split('+'))))
for i in range(1, len(divideList)):
    answer -= sum(list(map(int, divideList[i].split('+'))))
print(answer)
