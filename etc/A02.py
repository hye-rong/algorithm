def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        cur_min = len(s)
        tmp = ""
        cum = 1
        for start in range(0, len(s), i):
            cur_str = s[start:start + i]
            if tmp == cur_str:
                cum += 1
            else:
                if cum != 1:
                    cur_min -= i * (cum - 1) - len(str(cum))
                cum = 1
                tmp = cur_str
        if cum != 1:
            cur_min -= i * (cum - 1) - len(str(cum))
        if cur_min < answer:
            answer = cur_min

    return answer