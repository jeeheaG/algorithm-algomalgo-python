# v2 : MST - 크루스칼 알고리즘
# TS 1 : RecursionError - sys.setrecursionlimit(10**9) 로 해결
# TS 2 : 메모리 초과
#           -> union find 에서 find함수 작성 실수
#               find 재귀호출 시 find(root[v]) 이렇게 현재 노드의 루트값을 호출해줘야 경로압축이 된다!!기억해
#               그냥 find(v)하면 메모리 초과가 발생! 현재 함수랑 동일한 호출이라 그런듯함 (정확히 이해는 못했지만) 


'''
[문제 해석]

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

이번에는 크루스칼로 풀어본다

구상
- 간선을 모두 입력받고 가중치 오름차순으로 정렬해둠 (최소힙 써도 되긴 한데 잦은 추가삭제가 일어나는 게 아니라서.. 시간 공간 복잡도만 올라감)
- union find에 쓸 루트노드테이블 만듦
- 가장 가중치가 작은 간선을 확인함. 간선에 연결된 노드 추가 시 사이클이 생기지 않는지 union find로 두 노드의 루트노드 확인
    - 루트노드 다르면 추가 : 한쪽 노드로 넣어 루트노드테이블 갱신, 가중치 합 갱신, 추가된 간선 수 갱신
    - 로트노드 같으면 사이클 생기므로 추가하지 않고 넘어감
- 간선이 V-1개가 될 때까지 반복
'''

# import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) # TS 1

V, E = map(int, input().split())
root = [i for i in range(V+1)]

edge_cnt = 0
weight_sum = 0
heap = []

for _ in range(E) :
    v1, v2, w = map(int, input().split())
    # heapq.heappush(heap, (w, v1, v2))
    heap.append((w, v1, v2))

heap.sort()

def union(v1, v2) :
    if v1 == v2 :
        return
    root[find(v1)] = find(v2)

def find(v) :
    if root[v] != v :
        root[v] = find(root[v]) # TS 2
    return root[v]

# 크루스칼
for w, v1, v2 in heap :
    if edge_cnt == V-1 :
        break

    #루트가 같으면 넘어감
    if find(v1) == find(v2) :
        continue

    #루트가 다르면 그래프에 추가
    union(v1, v2)
    edge_cnt += 1
    weight_sum += w
    
# 크루스칼 - 최소힙 쓰는 경우의 코드
# while edge_cnt < V-1 :
#     w, v1, v2 = heapq.heappop(heap)

#     #루트가 같으면 넘어감
#     if find(v1) == find(v2) :
#         continue

#     #루트가 다르면 그래프에 추가
#     union(v1, v2)
#     edge_cnt += 1
#     weight_sum += w

print(weight_sum)