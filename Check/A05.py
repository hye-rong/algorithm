# 백준 1700번: 멀티탭 스케줄링

n, k = map(int, input().split())
order = list(map(int, input().split()))

find = [[] for _ in range(k)]
for i in range(k):
    find[order[i] - 1].append(i)

answer = 0
tab = [-1 for _ in range(n)]
for i in range(k):
    for j in range(n):
        if tab[j] == -1:
            tab[j] = order[i] - 1
            break
        elif tab[j] == order[i]-1:
            break
    else:  # 탭이 꽉 차있는 경우
        cur = 0
        maxNum = i
        for j in range(n):  # 탭에 있는 것 중에서
            for k in find[tab[j]]:  # 탭이 있는 위치
                if k > i: # 뒤에 나옴
                    if k > maxNum:  # 제일 뒤에 있는 것을 찾기
                        cur = j
                        maxNum = k
                    break
            else:  # 아예 나오지 않는다면 그것을 뺌
                cur = j
                break
        answer += 1
        tab[cur] = order[i] - 1
print(answer)
