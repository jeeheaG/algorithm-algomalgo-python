# v1 : bfs
#채점 되게 천천히 됨 쫄깃하네여..ㅎ
# TS 1 : 0%도 안뜨고 시간초과 뭘까??
#       -> 벽마다 bfs 돌면 시간초과 난다고 함
#            대신 미리 인접한 0들을 그룹으로 묶어 크기를 세두고, 벽마다 해당 벽과 인접한 0그룹들의 크기의 합으로 계산하기
# TS 2 : 인접한 그룹번호가 중복인 경우 놓쳤다 set으로 처리해줬음


'''
[문제 해석]
벽이 존재하는 맵이 주어짐. 각 벽마다 벽이 없어졌을 때, 해당 벽 위치에 인접한 공간 크기를 구하는 문제
- 빈 공간은 0, 벽은 1
- 벽 위치에 해당하는 공간 크기를 10으로 나눈 나머지를 출력
- 시간제한 : 2초

구상 2
- 전체를 돈다
- 방문 전인 빈 공간(0)이 나오면 bfs
    - 인접한 0들 그룹의 크기를 세어 저장해둔다.
    - 0 자리에는 해당되는 그룹번호를 적어둔다.
    - 그룹번호는 2부터 시작한다(0,1은 이미 사용중이므로)
- 0으로 초기화한 정답용 맵을 만든다.
- 다시 한 번 전체를 돈다
- 벽(1)이 나오면 해당 벽 상하좌우로 인접한 그룹번호들을 set에 넣어 중복을 제거하고, 그 그룹들의 크기의 합을 구한다
- 정답용 맵에 합을 10으로 나눈 나머지를 벽 위치에 기록한다.


구상 1(timeout)
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

grp_size_arr = [0,0] #그룹번호 2부터 시작

# 1. 0그룹 크기 세기 # TS 1
for i in range(N) :
    for j in range(M) :
        #벽이거나 이미 방문했으면 패스
        if board[i][j] != 0 :
            continue

        que = deque()
        que.append((i,j))
        
        grp_size_arr.append(0)
        grp = len(grp_size_arr) - 1
        board[i][j] = grp

        #bfs - 인접 0 그룹 크기 셈
        while que :
            x, y = que.pop()

            grp_size_arr[grp] += 1

            for dir in dir_arr :
                nx, ny = x+dir[0], y+dir[1]

                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 :
                    board[nx][ny] = grp
                    que.append((nx, ny))

# 2. 벽마다 인접 0그룹 크기 합 구하기
answer = [[0]*M for _ in range(N)]

for i in range(N) :
    for j in range(M) :
        if board[i][j] != 1 :
            continue
        
        grp_set = set()
        
        for dir in dir_arr :
            ni, nj = i+dir[0], j+dir[1]

            #인접 그룹번호 중복제거
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 1 :
                grp_set.add(board[ni][nj]) # TS 2

        #그룹 크기 합 구해서 기록
        size_sum = 1
        for grp in grp_set :
            size_sum += grp_size_arr[grp]

        answer[i][j] = size_sum%10

#출력
for line in answer :
    print(''.join(map(str, line)))