# v2 : 그래프(트리만 입력되는 경우)
#단절점, 단절선 개념


'''
[문제해석]
- 주어진 트리에서 각 노드, 간선이 단절점, 단절선인지 묻는 질문에 답 출력
- 질의 내용
    - t=1 일 때 : k번 정점이 단절점인가?
    - t=2 일 때 : k번째로 입력받았던 간선이 단절선인가?

개념
- 단절점, 단절선 : 특정 노드 또는 선을 제거했을 때 해당 그래프가 2개 이상으로 분리된다면 해당 노드 또는 선을 단절점 또는 단절선이라한다.
    DST(DFS Spanning Tree)를 활용해 단절점, 단절선을 판단할 수 있다.
- 트리 : 모든 노드가 연결되어있는, 사이클 없는 그래프
    -> 사이클이 없고 모든 노드가 연결되어있으므로,
        단절점 : 간선이 2개 이상 연결되어있는 노드는 모두 단절점임 (노드를 제거했을 때 간선이 1개면 해당 노드만 사라지지만 2개이상이면 이로인해 연결끊기는 노드 존재)
        단절선 : 모든 간선이 단절선임 (사이클없이 모두 연결되어있으므로)
    -> 결국 이 문제의 포인트는 트리의 특성을 이해하는 거였다,, 단절점을 곁들인

        
구상
- 트리 입력받고 간선 개수에 따라 단절점 여부 판단 (dfs도 필요없구나^.^!)
- 간선은 모두 단절선
'''

from collections import defaultdict
import sys
input = sys.stdin.readline

graph = defaultdict(list)
N = int(input())

#간선 입력받기
for _ in range(N-1) :
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 문제 입력받아서 답 출력
for _ in range(int(input())) :
    t, k = map(int, input().split())
    if t == 1 :
        print("yes" if 1 < len(graph[k]) else "no") #간선 개수로 단절점인지 판단
    elif t == 2 :
        print("yes") #모든 간선이 단절선