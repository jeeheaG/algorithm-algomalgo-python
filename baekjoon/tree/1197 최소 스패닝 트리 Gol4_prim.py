# v1 : MST - 프림 알고리즘
# TS : 메모리초과 - 노드 수가 10000정도면 직접 2차원 배열로 관리하는 건 메모리 상 힘들다고 함
#       -> 음.. 그래프 입력받는 걸 dict로 해야하나 - 해봤는데 시간초과
#       -> 통과된 다른 프림 코드 찾아봤는데 두가지를 나랑 다르게 함
#           1. list로 하되 v*v만큼 안쓰고 list를 dict처럼 썼음 i번째 인덱스에 i번노드의 간선들을 [노드번호, 노드와의 가중치] 이런 형태로 저장함
#           2. 그리고 간선 최솟값 구할 때 heap씀 : heap쓰면 그래프에 포함된 노드들에 대한 간선목록은 새로운 노드가 추가될때마다 다 힙에 때려넣어두면 됨!
#           => 통과~~ heap쓰니까 로직도 훨 깔끔하고 아주 맘에 든다^_^ 프림이 노드를 추가하는 방식이지만 결국은 간선의 가중치를 확인해야 하는데 논리를 너무 노드에만 집중해서 생각했다. 생각을 열어두자~
#               근데 크루스칼로 더 많이 푸시는 것 같다

'''
[문제 해석]
주어진 그래프의 최소 스패닝 트리MST를 구하는 문제
- 1 <= 정점V < 10000
- 1 <= 간선E < 100000
- 음수 가중치 간선 존재, 양방향
- 가중치 절댓값 < 1000000
- 시간 제한 1초
- 메모리 제한 128MB

[개념]
MST 구하는 법
1. 크루스칼 : 간선을 greedy로 선택, 사이클없이(union find)
2. 프림 : 노드를 선택. 노드 중 간선 가중치가 가장 적은 것

정점보다 간선 개수 범위가 더 커서 프림으로 짜보자

구상 1
- 간선 입력받아 리스트 i번째 인덱스에 i번째 노드의 간선들을 (가중치, 연결노드) 형태로 저장
- 사용 후보 간선 목록으로 최소 heap사용
- heap에 (0, 1)을 넣고 시작해 1번노드를 시작점으로 함
- heap에서 최소 간선을 pop해서 이미 추가된 노드인지 확인
    - 이미 있으면 넘어감
    - 아직 없으면 그래프에 추가하고, 그 새로운 노드의 간선들을 모두 heap에 추가함
- 추가된 노드 개수가 전체 노드 수만큼 될 때까지 반복
min heap 을 쓰니까 로직이 훨씬 깔끔해졌다!

구상 2 (메모리 초과)
- 간선 입력받아 2차원 리스트에 그래프 저장
- 1번 정점을 출발점으로, 그래프에 포함시킨다
- 그래프에 인접한 노드들 중 아직 그래프에 포함되어있지 않고, 연결된 간선 가중치가 가장 적은 노드를 그래프에 포함시킨다
- 모든 노드가 그래프에 포함되면 종료
'''

import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)] 
in_graph = [False]*(V+1)

for _ in range(E) :
    v1, v2, weight = map(int, input().split())
    graph[v1].append((weight, v2))
    graph[v2].append((weight, v1))

node_cnt = 0 #그래프에 포함된 노드 개수
weight_sum = 0

#그래프에 포함된 노드들에 인접한 간선 모음
edge_heap = [(0,1)] #가중치, 새로 추가될 노드번호
while node_cnt < V :
    w, node = heapq.heappop(edge_heap)

    #이미 그래프에 포함된 노드면 패스
    if in_graph[node] :
        continue

    #새로운 노드 추가
    in_graph[node] = True
    node_cnt += 1
    weight_sum += w

    #새로 추가된 노드의 간선들을 힙에 추가
    for edge in graph[node] :
        heapq.heappush(edge_heap, edge)

print(weight_sum)