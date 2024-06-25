# v2 : MST - kruscal (240ms)
# 간선 수가 노드수보다 100배 많은데 prim보다 kruscal이 더 빠르네

'''
[문제 해석]
최소의 비용으로 모든 컴퓨터를 연결하는 경로 구하기
= MST 최소 스패닝 트리 구하기
- 1 <= 컴퓨터 수N <= 1000
- 1 <= 간선 수M <= 100000
- 1 <= 가중치 <= 10000
- 간선이 주어질 때 두 노드번호가 같을 수도 있다

이번엔 크루스칼로 풀어보즈아~

구상
- 간선 입력받아서 (가중치, 노드1, 노드2) 형태로 한 리스트에 모두 저장
- 간선 가중치 오름차순으로 정렬
- 간선 리스트 돌면서 가장 가중치 작은 간선부터 사이클 생기는지 확인(union find)
    - 사이클 안 생기면 추가
    - 사이클 생기면 넘어감
- 간선 수 V-1개까지 반복
'''

import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

edges = []
for _ in range(E) :
    v1, v2, w = map(int, input().split())
    edges.append((w, v1, v2))

edges.sort()
edge_cnt = 0
weight_sum = 0

root = [i for i in range(V+1)]

def union(v1, v2) :
    # find(v1) == find(v2) 인 경우는 이미 union호출 전에 걸러졌음
    root[find(v2)] = root[find(v1)]

def find(v) :
    if root[v] != v :
        root[v] = find(root[v])
    return root[v]

for w, v1, v2 in edges :
    if edge_cnt == V-1 :
        break

    if v1 == v2 or find(v1) == find(v2) : 
        continue
    
    union(v1, v2)
    edge_cnt += 1
    weight_sum += w

print(weight_sum)
    