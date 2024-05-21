# https://school.programmers.co.kr/learn/courses/30/lessons/159993
# bfs 로!!!
# 2번의 bfs를 해줘야 함! : 시작 -> 레버, 레버 -> 출구

from collections import deque


def bfs(start, end, maps, row, col) :
    direc_arr = [(1,0), (0,1), (-1,0), (0,-1)]
    visited = [[False]*col for _ in range(row)]
    que = deque() # time 값도 같이 기록할 것임
    
    # 출발지 찾기 : 바로 time과 함께 큐에 넣음
    is_start_found = False
    for i in range(row) :
        for j in range(col) :
            if maps[i][j] == start :
                que.append((i,j,0)) # time 값을 함께 적어둠
                is_start_found = True
                break
        if is_start_found : break # 시작점 찾은 후론 더 안찾고 이중for문 탈출

    #bfs 시작
    while que :
        # print(que)
        item = que.popleft()

        for direc in direc_arr :
            cur = (item[0]+direc[0], item[1]+direc[1], item[2]) # 현재 위치의 주변 좌표로 이동

            # 지도 범위 내인지 확인
            if 0 <= cur[0] < row and 0 <= cur[1] < col :
                #탐색
                cur_val = maps[cur[0]][cur[1]]
                
                #목적지라면 time을 반환하고 이번 bfs 종료 -> 이게 for문 밖으로 나와도 되나?
                if cur_val == end :
                    # print('found '+end)
                    return cur[2]+1
                
                #벽이 아니고 아직 방문 전이라면 지나가기 가능
                if cur_val != 'X' and not visited[cur[0]][cur[1]] :
                    # print('is not wall')
                    que.append((cur[0], cur[1], cur[2]+1)) # time에 +1해서 방문 후보 큐에 등록
                    visited[cur[0]][cur[1]] = True

    # 목적지에 도달하지 못했다면 -1 반환
    return -1 

def solution(maps):
    row, col = len(maps), len(maps[0])

    time_lever = bfs('S', 'L', maps, row, col)
    time_exit = bfs('L', 'E', maps, row, col)

    # 둘다 -1이 아니라면 최단거리의 합이 최종 최단거리
    if time_lever != -1 and time_exit != -1 : 
        return time_lever + time_exit
    else :
        return -1   

# print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
# print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))
print(solution(["SOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOLE"])) #런타임에러 반례 : 리스트 인덱싱 아웃