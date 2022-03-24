# 백준 16916번: 부분 문자열

s = input()
p = input()

# 접두사 접미사 일치 정보 알기
def makeTable(pattern):
    table = [0 for _ in range(len(pattern))]
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

def KMP(parent, pattern):
    table = makeTable(pattern)
    j = 0
    for i in range(0, len(parent)): # 계속해서 이동함
        while j > 0 and parent[i] != pattern[j]: # 점프
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                return 1
            else:
                j += 1 # 계속해서 매칭이 이뤄지는지 확인
    return 0


print(KMP(s, p))