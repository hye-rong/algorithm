# 프로그래머스 구명보트
import heapq
def solution(people, limit):
    answer = 0
    light = []
    heavy = []
    for p in people:
        if p <= limit / 2:
            heapq.heappush(light, p)
        else:
            heapq.heappush(heavy, -p)

    answer += len(heavy)
    while len(heavy) != 0 and len(light) != 0:
        if light[0] - heapq.heappop(heavy) <= limit:
            heapq.heappop(light)
    answer += (len(light) + 1) // 2

    return answer