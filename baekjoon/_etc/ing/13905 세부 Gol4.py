# v1 : MST

'''
[문제 해석]
출발 노드에서 도착 노드로 가는 경로 중, 거치는 간선 가중치의 최솟값이 가장 큰 경로를 구하기
- 시간 제한 1초


[솔루션 목록]

1. (시간초과)
bfs 돌면서 간선 최소값 들고다님
도착노드 만나면 bfs 종료, 간선 최소값을 그동안의 값이랑 비교해 최댓값구함
- 시간제한 : 1초
- N <= 10^5, M <= 3 * 10^5
    -> 그냥 bfs하면 시간초과

2.
크루스칼로 MST(Maximum)를 만들어둔 후에, 시작노드부터 도착노드까지의 bfs를 함
-> 오.. 기억해놓자 MST를 경로에 활용하는 법..
=> 요걸로 풀어본다

3. 
다익스트라

4. 
이분탐색 + BFS
무게 최대값을 찾기 위해 가능한 무게를 1~제한값 범위에서 이분탐색함. BFS돌면서 가능한지 확인함
-> ㅎ..ㄷㄷ



[구상] 
MST(Max) 를 구해놓은 뒤, 그 경로에서 bfs로 출발노드->도착노드 경로의 최소가중치를 구한다!

MST
- 간선 입력 받음. (가중치, 노드, 노드)
- Max니까 큰 순으로 정렬함
- union, find 함수 만듦
    - union : find로 중복인지 확인 후 간선먹음(트리합침)
    - find : 루트노드가 같은지 확인. 같으면 사이클생기므로 뱉음. with 경로압축
- 수행하면서 겹치지 않게 간선 먹음
- 간선 N-1개 먹었으면 끝

BFS
- MST에 사용된 간선만 탐색해서 출발->도착 경로 찾음
- 이 때 경로 최소 가중치 들고다님. 찾은 경로의 최소가중치가 답

'''

from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split()) # 출발, 도착 노드

edges = [tuple(map(int, input().split())) for _ in range(M)]

edges.sort(key = lambda x : x[2], reverse=True) # 원소의 세번째 값을 기준으로, 거꾸로 정렬하라


## union find
# x, y 트리 합치기
def union(x, y) :
    if x==y :
        return
    parent[find(x)] = find(y) # 루트끼리 합칠 것!!!

# rank = [1]*(N+1)
# def union_by_rank(x, y) :
#     if x==y :
#         return
    
#     if rank[x] < rank[y] :
#         union(x, y)
#         rank[y] = rank


# x 의 루트 찾기(재귀)
def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]


## MST 만들기 - 크루스칼

parent = [i for i in range(N+1)] # 각 노드의 루트노드 기록
new_edges = []
for edge in edges :
    if len(new_edges) >= N-1 :
        break

    n1, n2, w = edge
    if find(n1) != find(n2) : # 루트노드가 다르면 = 트리가 다르면 = 사이클이 안생기면
        union(n1, n2)
        new_edges.append((edge))

# print(new_edges)

## 이제 bfs 로 출발-도착 경로찾기

edge_dict = defaultdict(list)
for n1, n2, w in new_edges :
    edge_dict[n1].append((n2, w))
    edge_dict[n2].append((n1, w))

que = deque()
que.append((S, 0, int(2e9))) # 시작노드 넣어주기 (다음노드, 가중치, 최소가중치)

ans = 0
while que :
    n, w, min_w = que.popleft()

    if n == E :
        ans = min_w
        break

    for n, w in edge_dict[n] :
        que.append((n, w, min(min_w, w)))

print(ans)


