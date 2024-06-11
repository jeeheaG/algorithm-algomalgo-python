# v1 : 그래프
#단절점, 단절선 개념
#단절점 단절선 찾기 로직 이해하느라 한참걸렸다.. 나 이런거에 약해


'''
[문제해석]
- 주어진 트리에서 각 노드, 간선이 단절점, 단절선인지 묻는 질문에 답 출력
- 질의 내용
    - t=1 일 때 : k번 정점이 단절점인가?
    - t=2 일 때 : k번째로 입력받았던 간선이 단절선인가?

구상
- 트리 입력받고..
- 노드마다 직접 끊어보고 그래프 분리되었는지 확인하기? -> 가능은 한데 오래걸림 O(v(v+e))
- 특정 노드, 간선이 단절점, 단절선인지 판단하는 법 -> 찾아보니까 방법이 따로 있음. 그래프 입력받고나서 미리 판단해둔 후에 질의에 따라 출력

개념
- 단절점, 단절선 : 특정 노드 또는 선을 제거했을 때 해당 그래프가 2개 이상으로 분리된다면 해당 노드 또는 선을 단절점 또는 단절선이라한다.
    DST(DFS Spanning Tree)를 활용해 단절점, 단절선을 판단할 수 있다.
    - 단절점 판단법 O(v+e)
        1. dfs 로 내려가며 방문번호 매김
        2. 돌아나올 때, 내 short 값과 부모노드를 포함한 인접노드들의 방문번호 중 최솟값을 short값으로 기록하고, 다음 노드에 전파하면서 돌아나옴
        3. 전파받은 short값이 현재 short값보다 작으면 그걸로 갱신. 만약 현재 방문번호와 전파받은 short값이 같으면 해당 노드는 단절점!
        +) 루트 노드는 자식이 2개 이상이면 무조건 단절점임. 따로 처리해줄 것
    - 단절선 판단법 (단절점 판단법과 유사함. 달라지는 부분은 ""로 감쌌음!) O(v+e)
        1. dfs 로 내려가며 방문번호 매김
        2. 돌아나올 때, 내 short 값과 "부모노드를 제외한" 인접노드들의 방문번호 중 최솟값을 short값으로 기록하고, 다음 노드에 전파하면서 돌아나옴
        3. 전파받은 short값이 현재 short값보다 작으면 그걸로 갱신. 만약 "현재 방문번호보다 전파받은 short값이 크면" 그 사이 간선은 단절선!
'''

from collections import defaultdict
import sys
input = sys.stdin.readline
INF = int(2e9)

graph = defaultdict(list)
edge_num = dict() #답 출력을 위해 몇번째로 입력받은 간선인지 저장해둬야 함
N = int(input())

#간선 입력받기
for i in range(1, N) :
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

    edge_name = ' '.join(map(str, sorted([n1, n2]))) #일관적인 간선 네이밍을 위해 간선 숫자순으로 정렬해서 문자열로 변환해 키값 사용
    edge_num[edge_name] = i # i번째로 입력받은 간선


nums = [[INF]*2 for _ in range(N+1)] # i번째 인덱스에 i번 노드의 정보를 담음. 0번째 값은 방문번호, 1번째 값은 short값
visited = [False]*(N+1)
cut_vertex = [False]*(N+1) #단절점인지 기록

# 단절점 dfs
def vertex_dfs(cur, visit_num) :
    #방문번호 매김
    nums[cur][0] = visit_num

    #자식노드 dfs
    for node in graph[cur] :
        if not visited[node] : #방문했던 노드가 아니면
            visited[cur] = True
            new_short = vertex_dfs(node, visit_num+1)
            
            #전파받은 short값 기존값과 비교 후 갱신
            nums[cur][1] = min(nums[cur][1], new_short)
            #전파받은 short값이 현재 노드의 방문번호와 같다면 단절점!
            if nums[cur][0] == new_short :
                cut_vertex[cur] = True

    #돌아나오기 - 내 short값을 인접노드 방문번호들과 비교해 최솟값으로 갱신
    for node in graph[cur] :
        nums[cur][1] = min(nums[cur][1], nums[node][0])

    return nums[cur][1]


vertex_dfs(1, 1)

# 루트 노드는 따로 판단해줌
root = 1
cut_vertex[root] = True if 1 < len(graph[root]) else False

# print(cut_vertex)


### 단절선 판단 ###

nums = [[INF]*2 for _ in range(N+1)]
visited = [False]*(N+1)
cut_edge = [False]*(N) # i번 인덱스에 i번째로 입력받은 간선이 단절선인지 기록

# 단절선 dfs
def edge_dfs(cur, visit_num, parent) :
    #방문번호 매김
    nums[cur][0] = visit_num

    # 인접노드 dfs
    for node in graph[cur] :
        if not visited[node] :
            visited[node] = True
            new_short = edge_dfs(node, visit_num+1, cur)
        
            #새로운 short 값 전파받기
            nums[cur][1] = min(nums[cur][1], new_short)

            #현재 방문번호보다 전파받은 short 값이 더 크면 그 사이 간선은 단절선!
            if nums[cur][0] < new_short :
                edge_name = ' '.join(map(str, sorted([cur, node])))
                # print(edge_name)
                idx = edge_num[edge_name]
                cut_edge[idx] = True

    #부모노드를 제외한 인접노드들의 방문번호와 현재노드의 short 값 비교해 갱신
    for node in graph[cur] :
        if node == parent :
            continue
        nums[cur][1] = min(nums[cur][1], nums[node][0])
    
    return nums[cur][1]

edge_dfs(1, 1, 0)

# print(cut_edge)


# 문제 입력받아서 답 출력
for _ in range(int(input())) :
    t, k = map(int, input().split())
    if t == 1 :
        print("yes" if cut_vertex[k] else "no")
    elif t == 2 :
        print("yes" if cut_edge[k] else "no")