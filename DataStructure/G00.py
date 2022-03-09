# 백준 1158번: 요세푸스
# 큐를 이용하는 방법으로 변경
# 리스트에서 index로 삭제하는 대신, 큐를 이용해서 popLeft 후에 삽입을 반복해서 구현
# rotate 함수를 이용하면 자동으로 되고 시간도 빠르다
# 큐를 이용하지 않은 경우 시간 복잡도는 o(N^2)
# 큐를 이용한 경우 시간 복잡도는 O(KN)
# K<=N 이기 때문에 크게 차이나지 않지만 K와 N이 차이가 많이나는 경우에는 차이가 있다


from collections import deque

n, k = map(int, input().split())
answer = []
q = deque()
for i in range(1, n+1):
    q.append(i)

while q:
    q.rotate(-k) # 왼쪽으로 k번 rotate
    answer.append(str(q.pop()))


print("<",", ".join(answer), ">", sep='')

