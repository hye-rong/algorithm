# 단속카메라
def solution(routes):
    answer = 0
    routes = sorted(routes)
    end = -30001
    for car in routes:
        if car[0] <= end:
            end = min(car[1], end)
        else:
            answer += 1
            end = car[1]

    return answer