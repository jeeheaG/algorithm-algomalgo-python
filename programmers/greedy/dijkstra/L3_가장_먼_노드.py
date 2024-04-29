# v1 : 다익스트라 (그래프 - 딕셔너리 사용)
#그래프. 1번에서 가장 먼 노드의 갯수 -> 모든 노드와의 거리를 구해야 함. 음의간선 없음 = 다익스트라
#간선값이 모두 동일하므로 딕셔너리를 써보자!

from collections import defaultdict
import heapq

INF = int(2e9)

def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    min_dist_arr = [INF]*(n+1)
    min_dist_arr[0] = 0
    min_dist_arr[1] = 0 #출발지
    
    heap = []
    heapq.heappush(heap, (0,1)) #(거리, 노드번호)
    
    # 그래프 입력 - 딕셔너리
    for e in edge :
        start, end = e
        graph[start].append(end)
        graph[end].append(start) #양방향 간선, 가중치 모두 동일
    
    #인접노드 탐색 시작
    while heap :
        cur_dist, cur_node = heapq.heappop(heap)
        
        for next_node in graph[cur_node] :
            #인접노드의 현재 최단거리보다 현재 노드를 거쳐가는 게 빠르면 갱신, 힙 푸시
            new_dist = cur_dist+1
            if new_dist < min_dist_arr[next_node] :
                min_dist_arr[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
    
    #제일 먼 값 구함
    max_dist = max(min_dist_arr)
    
    #제일 먼 노드 수 구함
    max_node_arr = [x for x in min_dist_arr if x==max_dist]
    answer = len(max_node_arr)
    
    return answer