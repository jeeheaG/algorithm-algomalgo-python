#다익이라면.. 부분최적구조로 생각.. 해당 노드까지의 최적경로가 아니라 intentsity최대값을 구해놓으면 되려나?
#모든 봉우리에 대해 다익스트라를 하는데, 산봉우리거나 출입구이면 탐색 안함
# TS : test case 2/4
# TS : 자잘한 실수 줄이기 . . (결과 반환 형식 확인, 부등호 헷갈리기x)

#[문제해석]
#n개 = 출/쉼/산봉. 등산로로 이동
#등산코스. 쉼/산봉 = 휴식, 휴식없이 intensity
#출-산봉-출, 1산봉, 쉼터 껴서 intensity최소. 같은 출입구로 올 것
#**intensity최소가 여러개라면 산봉번호가 낮은 걸로 반환


import heapq
INF = int(2e9)

def solution(n, paths, gates, summits):
    intensity_summits = [] #(intensity, summmit)
    
    #경로를 그래프테이블에 담음
    graph = [[INF]*(n+1) for _ in range(n+1)]
    
    for path in paths :
        i, j, w = path
        graph[i][j] = w
        graph[j][i] = w #양방향 간선
    
    #모든 봉우리에 대해, 모든 출발지에 대해 다익스트라
    for summit in summits :
        summit_min_intensity = INF
        for gate in gates :
            intensity_arr = [INF]*(n+1)
            intensity_arr[summit] = 0 #출발지
            
            heap = []
            heapq.heappush(heap, (0, gate)) #(최대 intensity, 지점번호)

            #인접 노드 탐색
            while heap :
                cur_intensity, cur_node = heapq.heappop(heap)
                
                for next_node in range(1, n+1) :
                    #출입구이면 탐색 안함
                    if next_node in gates :
                        continue
                    #현재 산봉우리 외에 다른 산봉우리면 탐색 안함
                    if next_node in summits and next_node != summit :
                        continue
                    # print(cur_node, next_node)
                    
                    #인접노드이면
                    edge = graph[cur_node][next_node]
                    # print(cur_weight)
                    if edge != INF :
                        new_intensity = max(cur_intensity, edge)
                        if new_intensity < intensity_arr[next_node] :
                            print("push : (", new_intensity, ", ", next_node, ")")
                            intensity_arr[next_node] = new_intensity
                            heapq.heappush(heap, (new_intensity, next_node))
        
            # new_intensity_arr = [x for x in intensity_arr if x != INF]
            # gate_max_intensity = max(new_intensity_arr)
            print(intensity_arr)
            gate_max_intensity = intensity_arr[summit] #출입구에서 봉우리까지 갈 때의 최대 intensity
            if gate_max_intensity < summit_min_intensity :
                summit_min_intensity = gate_max_intensity
        
        heapq.heappush(intensity_summits, (summit_min_intensity, summit))
        
    #전체 봉우리 중 최대 intensity가 제일 작은 봉우리 반환 -> 우선순위큐(heapq)에 넣어둬서 맨 첫 요소 pop
    print(intensity_summits)
    ans_intensity, ans_summit = heapq.heappop(intensity_summits)
    answer = [ans_summit, ans_intensity]
    
    return answer

# print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])) #[5,3]

print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])) #[3, 4]
# print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5])) #[5, 1]

# print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5])) #[5, 6]