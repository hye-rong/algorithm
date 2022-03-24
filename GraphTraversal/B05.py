# 백준 13549번: 숨바꼭질 3
# 가장 빠른 시간을 구하기 때문에 bfs
# 하지만 순간이동을 하는 것은 시간이 증가하지 않으므로
# 우선순위 큐를 이용해야 한다.
# visited를 관리할 때 +1해서 가는것이 *2해서 가는 것보다
# 먼저 체크되면 답이 +1 해서 나올 수 있다
# 여기서도 우선순위 고려

import heapq

n, k = map(int, input().split())

visited = [0 for _ in range(100001)]


def bfs(n, k):
    heap = []
    heapq.heappush(heap, (0, n))
    visited[n] = 1
    while heap:
        cnt, a = heapq.heappop(heap)
        print(cnt, a)
        if a == k:
            print(cnt)
            break
        if 0 <= a * 2 <= 100000 and visited[a * 2] == 0:
            visited[a * 2] = 1
            heapq.heappush(heap, (cnt, a * 2))
        if 0 <= a + 1 <= 100000 and visited[a + 1] == 0:
            heapq.heappush(heap, (cnt + 1, a + 1))
            visited[a + 1] = 1
        if 0 <= a - 1 <= 100000 and visited[a - 1] == 0:
            visited[a - 1] = 1
            heapq.heappush(heap, (cnt + 1, a - 1))



bfs(n, k)
