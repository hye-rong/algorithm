# 백준 2887번: 행성 터널
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

n = int(input())
parent = [0] * n
for i in range(n):
    parent[i] = i

node = []
for i in range(n):
  x, y, z = map(int, input().split())
  node.append([x, y, z, i])

sortByX = sorted(node, key = lambda x : x[0])
sortByY = sorted(node, key = lambda x : x[1])
sortByZ = sorted(node, key = lambda x : x[2])

edges = []
for i in range(1, n):
  edges.append([sortByX[i][0] - sortByX[i-1][0], sortByX[i][3], sortByX[i-1][3]])
  edges.append([sortByY[i][1] - sortByY[i-1][1], sortByY[i][3], sortByY[i-1][3]])
  edges.append([sortByZ[i][2] - sortByZ[i-1][2], sortByZ[i][3], sortByZ[i-1][3]])

edges.sort()

result = 0
count = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
        count += 1
        if count == n-1:
          break

print(result)