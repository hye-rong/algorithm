# 백준 1715번: 카드 정렬하기

import sys
import heapq

n = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(n)]
heapq.heapify(cards)
answer = 0
while len(cards) != 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a+b)
    answer += a + b
print(answer)
