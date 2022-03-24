# 백준 1197번: 최소 스패닝 트리

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
parent = [i for i in range(v+1)]

edges = sorted(edges, key=lambda x: x[2])
answer = 0
for e in edges:
    a, b, c = e
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += c

print(answer)


