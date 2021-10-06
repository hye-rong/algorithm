# 프로그래머스 2019 KAKAO 실패율

def solution(N, stages):
    answer = []
    fail = []
    stages.sort()

    base, stay = 0, 0
    for i in range(N):
        while base + stay < len(stages):
            if stages[base + stay] == i + 1:
                stay += 1
            else:
                break
        if len(stages) == base:
            fail.append([i + 1, 0])
        else:
            fail.append([(i + 1), stay / (len(stages) - base)])
        base += stay
        stay = 0
    fail = sorted(fail, key=lambda x: (-x[1], x[0]))
    answer = [f[0] for f in fail]

    return answer