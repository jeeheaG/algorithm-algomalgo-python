# timeout : bfs
# TS : 0%도 안뜨고 시간초과 뭘까??
#       -> 벽마다 bfs 돌면 시간초과 난다고 함
#            대신 미리 인접한 0들을 그룹으로 묶어 크기를 세두고, 벽마다 해당 벽과 인접한 0그룹들의 크기의 합으로 계산하기

'''
[문제 해석]
벽이 존재하는 맵이 주어짐. 각 벽마다 벽이 없어졌을 때, 해당 벽 위치에 인접한 공간 크기를 구하는 문제
- 빈 공간은 0, 벽은 1
- 벽 위치에 해당하는 공간 크기를 10으로 나눈 나머지를 출력
- 시간제한 : 2초

구상
- 전체를 돈다
- 벽(1)이 나오면 해당 벽에 인접한 공간을 bfs 돌며 공간 크기를 계산한다
- 벽 위치에 공간 크기를 10으로 나눈 나머지를 기록한다
'''

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, list(input().strip()))) for _ in range(N)]
dir_arr = [(0,1), (1,0), (-1,0), (0,-1)]

for i in range(N) :
    for j in range(M) :
        #빈 공간은 패스
        if board[i][j] == 0 :
            continue

        que = deque()
        que.append((i,j))

        visited = [[False]*M for _ in range(N)]
        visited[i][j] = True
        
        cnt = 1

        #bfs - 인접 공간 크기 셈
        while que :
            x, y = que.pop()

            for dir in dir_arr :
                nx, ny = x+dir[0], y+dir[1]

                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and not visited[nx][ny] :
                    visited[nx][ny] = True
                    cnt += 1
                    que.append((nx, ny))

        #벽 위치에 공간 크기를 기록
        board[i][j] = cnt%10

#출력
for line in board :
    print(''.join(map(str, line)))