# v1 : 다익스트라
# think : 최단거리가 3이하인 모든 마을을 알아내는 문제 -> 모든 노드로의 최단경로 구하기, 음의 간선 없음 = 다익스트라

import heapq
INF = int(2e9)

def solution(N, road, K):
    answer = 0

    graph = [[INF]*(N+1) for _ in range(N+1)]
    min_dist = [INF]*(N+1)
    min_dist[1] = 0 #출발지
    heap = []

    #간선정보를 그래프 테이블에 담음
    for road_item in road : 
        start, end, dist = road_item

        if dist < graph[start][end] :
            graph[start][end] = dist
            graph[end][start] = dist #양방향 간선


    heapq.heappush(heap, (0,1)) # 출발지 넣어줌 - (거리, 노드번호)

    while heap :
        cur_dist, cur_node = heapq.heappop(heap)

        #인접노드 탐색
        for next_node in range(1, N+1) :
            if graph[cur_node][next_node] != INF :
                new_dist = cur_dist + graph[cur_node][next_node]
                #출발지에서 해당노드까지 가는 거리가 현재의 최단거리보다 작을 경우
                if new_dist < min_dist[next_node] :
                    min_dist[next_node] = new_dist #최단거리를 갱신
                    heapq.heappush(heap, (new_dist, next_node)) #새 경로를 힙에 넣음
                
    # 최단거리가 K이하인 노드 개수 반환
    for d in min_dist :
        if d <= K : answer+=1

    return answer


# 테스트
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
# print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))