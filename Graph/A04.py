# 백준 1197번: 최소 스패닝 트리
import sys

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union_parent(a, b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b:
      parent[b] = a
  else:
    parent[a] = b


input = sys.stdin.readline

v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]

# 초기화
parent = [0] * (v + 1)
for i in range(v + 1):
    parent[i] = i

edges = sorted(edges, key=lambda x: x[2])
result = 0
for edge in edges:
    a, b, c = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += c
print(result)


