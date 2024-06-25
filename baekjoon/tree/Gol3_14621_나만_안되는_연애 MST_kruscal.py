# v1 : MST - kruscal

'''
[문제해석]
모든 대학교를 연결하는 최단경로 = MST
- 남초대학교M 와 여초대학교W 사이의 간선만 경로에 포함할 수 있음
- 모든 학교를 연결하는 경로가 존재하지 않을 경우 -1 출력
- 1 <= 학교 수V <= 1000
- 1 <= 간선 수E <= 10000

크루스칼~로 해보자
특이사항은 간선 선택할 때, 연결된 노드의 학교종류가 같으면 선택하지 않도록 짜면 될 듯

구상
- 간선 (가중치, 노드1, 노드2) 형식으로 한 리스트에 입력받음
    - 이 때 노드1과 노드2의 학교타입이 같으면 리스트에 넣지 않음 (그래프에 사용할 수 없는 간선이므로)
- 가중치 오름차순 정렬
- kruscal 로 경로 생성 : union find로 사이클이 없는지 확인하며 간선을 greedy하게 선택
- 간선 개수가 V-1개일 때까지 반복
'''

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
school_type = ("0", ) + tuple(input().split()) # 0번째 인덱스는 사용하지 않음

edges = []
for _ in range(E) :
    v1, v2, w = map(int, input().split())
    
    #같은 타입의 학교이면 해당 간선은 사용하지 않음
    if school_type[v1] == school_type[v2] :
        continue
    edges.append((w, v1, v2))

edges.sort()

edge_cnt = 0
weight_sum = 0
root = [i for i in range(V+1)]

# union find
def union(v1, v2) :
    #find(v1) == find(v2) 인 경우는 호출 전에 걸러졌음
    root[find(v1)] = root[find(v2)]

def find(v) :
    if root[v] != v :
        root[v] = find(root[v])
    return root[v]

# kruscal
for w, v1, v2 in edges :
    if V-1 <= edge_cnt :
        break

    if find(v1) == find(v2) :
        continue

    union(v1, v2)
    edge_cnt += 1
    weight_sum += w

print(weight_sum if edge_cnt == V-1 else -1)

