# 백준 1647번: 도시분할계획
import sys
input = sys.stdin.readline

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

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
edges = sorted(edges, key=lambda x: x[2])

parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i

result = 0
count = 0
for edge in edges:
    a, b, cost = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
        count += 1
        if count == n - 2:
            break

print(result)

