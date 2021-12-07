# 백준 1969번: DNA
import sys

input = sys.stdin.readline


n, m = map(int, input().split())
dnaList = [input() for _ in range(n)]

answerChar = ''
answerNum = 0
for k in range(m):  # 문자열들의 같은 번째 문자 확인
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(n):
        dic[dnaList[i][k]] += 1
    maxNum = 0
    tmp = ''
    for d in dic:
        if dic[d] > maxNum:
            tmp = d
            maxNum = dic[d]
    answerChar += tmp
    answerNum += n - maxNum

print(answerChar)
print(answerNum)