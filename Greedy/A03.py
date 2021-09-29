
#체육복
def solution(n, lost, reserve):
    answer = 0
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for item in sorted(reserve_set):
        if item - 1 in lost_set:
            lost_set.remove(item - 1)
        elif item + 1 in lost_set:
            lost_set.remove(item + 1)
    answer = n - len(lost_set)
    return answer