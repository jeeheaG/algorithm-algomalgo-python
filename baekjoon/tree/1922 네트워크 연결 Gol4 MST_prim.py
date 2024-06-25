# v1 : MST - prim
# TS : 양방향 간선 까먹지 말그라

'''
[문제 해석]
최소의 비용으로 모든 컴퓨터를 연결하는 경로 구하기
= MST 최소 스패닝 트리 구하기
- 1 <= 컴퓨터 수N <= 1000
- 1 <= 간선 수M <= 100000
- 1 <= 가중치 <= 10000
- 간선이 주어질 때 두 노드번호가 같을 수도 있다

MST 프림으로 풀어보자~ 노드선택

구상
- 간선 입력받아서 연결된 첫번째 노드별로 (가중치, 노드2) 형태로 리스트에 저장
- 최소힙 사용(정렬유지하며 잦은 삽입 필요)
- 현재 그래프에 포함되어있는 노드 표시하는 배열 사용
- 현재 그래프와 인접한 간선들을 최소힙에 넣음
- 최소힙에서 가장 가중치 적은 노드 pop해서 추가될 노드가 현재 그래프에 포함되어있는 노드인지 확인
    - 사이클 안 생기면 추가
    - 사이클 생기면 넘어감
- 간선 수 V-1개까지 반복
'''

import heapq
import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

edges = [[] for _ in range(V+1)] # i번 인덱스에 i번 노드와 연결된 간선을 (가중치, 노드2) 형태로 저장

for _ in range(E) :
    v1, v2, w = map(int, input().split())
    if v1 == v2 : 
        continue # 같은 노드를 잇는 간선은 넘어감

    edges[v1].append((w, v2))
    edges[v2].append((w, v1)) # TS

heap = []
heap.append((0,1))
in_graph = [False]*(V+1)
edge_cnt = -1
weight_sum = 0

while edge_cnt < V-1 :
    w, v2 = heapq.heappop(heap)

    if in_graph[v2] :
        continue

    in_graph[v2] = True
    edge_cnt += 1
    weight_sum += w
    for edge in edges[v2] :
        heapq.heappush(heap, edge)

print(weight_sum)