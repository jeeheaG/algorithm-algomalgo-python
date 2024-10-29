# v1 : union find / bfs dfs

'''
[문제해석]
주어진 그래프가 몇 개의 연결된 요소로 되어있는지 구하기

[구상]
union find 써서 그래프 연결
루트노드 유니크 개수 출력

아니면 노드별로 bfs/dfs 돌면서 방문체크하고 새로 bfs 시작할 때마다 개수세도 됨

'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = [[False]*(N+1) for _ in range(N+1)]

for _ in range(M) :
    n1, n2 = map(int, input().split())
    edges[n1][n2] = True
    edges[n2][n1] = True

root = [i for i in range(N+1)]

# x, y 가 포함된 그래프 union
def union(x, y) :
    if x == y :
        return 
    root[find(x)] = find(y) # y의 루트 밑으로 x의 루트를 넣음
    
# x의 루트 find
def find(x) :
    if x != root[x] :
        root[x] = find(root[x]) # 경로 압축
    return root[x]

# 간선 순회하며 union find
for i in range(1, N+1) :
    for j in range(1, N+1) :
        if edges[i][j] and find(i) != find(j):
            union(i, j)

# 루트노드 구해서 set에 넣고 set 크기 계산
root_set = set()
for n in range(1, N+1) :
    root_set.add(find(n))

print(len(root_set))
        