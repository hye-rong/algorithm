import heapq

# 무지의 먹방 라이브
# heap 사용

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1

    food_heap = []
    cur_len = len(food_times)
    for i in range(cur_len):
        heapq.heappush(food_heap, (food_times[i], i + 1))

    min_round = food_heap[0][0]

    while k >= cur_len * min_round:
        k -= cur_len * min_round
        while True:
            (min_count, num) = heapq.heappop(food_heap)
            cur_len -= 1
            if min_count != food_heap[0][0]:
                min_round = food_heap[0][0] - min_count
                break
    food_heap = sorted(food_heap, key=lambda x: x[1])
    answer = food_heap[k % cur_len][1]

    return answer
