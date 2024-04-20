# v1 : bfs
# bfs로만 풀리는 문제. dfs는 효율성 제한 걸림

from collections import deque
INF = int(2e9)

def solution(maps):
    min_time = INF
    
    size_n, size_m = len(maps), len(maps[0])
    
    visited = [[False]*(size_m) for _ in range(size_n)]
    visited[0][0] = True
    direc_arr = [(1,0), (0,1), (-1,0), (0,-1)]

    que = deque()
    que.append((0,0,1)) # n, m, time

    while que :
        n, m, time = que.popleft()
        
        #목적지인지 확인
        if n == size_n-1 and m == size_m-1 :
            if time < min_time :
                min_time = time
    
        #목적지가 아니면 주변 칸들 탐색
        else :
            for direc in direc_arr :
                next_n = n+direc[0]
                next_m = m+direc[1]
                #방문 전이면서 프레임 내인 칸만 탐색
                if 0 <= next_n < size_n and 0 <= next_m < size_m and not visited[next_n][next_m] :
                    if maps[next_n][next_m] == 1 :
                        visited[next_n][next_m] = True
                        que.append((next_n, next_m, time+1))

    if min_time == INF :
        return -1
    else : return min_time


# 테스트
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))