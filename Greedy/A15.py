# 백준 1700번: 멀티탭 스케줄링
# 가장 늦게 나오는 것 빼야 함

n, k = map(int, input().split())
seq = list(map(int, input().split()))

priority = [[] for _ in range(k+1)]
tab = [0 for _ in range(n)]

def find_tab(after): # 멀티탭에서 빼야 되는 곳 index 반환
    maxNum = 0
    idx = 0
    for i in range(len(tab)):
        for j in priority[tab[i]]:
            if j > after: # 현재 진행보다 뒤에 존재하는 숫자 중
                if j > maxNum: # 제일 멀리 있는 번호 갱신
                    idx = i
                    maxNum = j
                break
        else: # 뒤에 등장하지 않는 번호면 바로 return
            return i
    return idx # 제일 멀리 있는 번호 return

# 숫자 별로 몇번째 나오게 되는지 저장
for i in range(len(seq)):
    priority[seq[i]].append(i)

answer = 0
for i in range(len(seq)):
    for j in range(len(tab)): # 빼지 않아도 되는 경우
        if tab[j] == 0 or tab[j] == seq[i]:
            tab[j] = seq[i]
            break
    else:
        index = find_tab(i)
        tab[index] = seq[i]
        answer += 1

print(answer)