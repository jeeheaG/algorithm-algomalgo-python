# v1 : bfs
# TS 1 : 시간초과(pypy도) - 더 걸러낼 조건이 있나..?
#       1. min_cnt_arr 위치 bfs밖으로 변경
#       2. (x) 사이드 기록해놓고 그것만 돌기? 이건 사이드인지 확인하는 위치만 달라져서 어차피 비슷할 거 같음
#       3. (x) 사이드 기록해놓고 아예 각 사이드 사이의 거리를 계산(bfs x)
#       4. (x) 다른 분들 코드 보니까 두번째 bfs에서 bfs의 while문이 이중for문 밖에 나와있음. 어?
#           -> 똑같은데서 시간초과 
#       5. TS 2 가 문제였음
# TS 2 : 코드 오류 수정으로 시간복잡도 개선(pypy통과, python 57%)
#       -> 두번째 bfs의 while문 안에서 주변노드 탐색할 때 최소이동횟수 비교하는 조건문을 잘못 적었음..,,,.. cnt+1을 그냥 cnt로 적어놔서 수정함



'''
[문제 해석]
- 땅과 땅을 연결하는 가장 짧은 다리 길이 찾기
- 다리와 인접해있으면 연결된 것임
- 시간제한 2초


구상
전체를 2번 돌아야 할 듯?

1. 같은 땅끼리 표시하기
- 전체를 돈다
- 땅(1)이 나오면 bfs돌며 땅번호를 붙이면서 visited 표시한다
- 땅 번호는 2부터 시작(0,1이 이미 사용중이므로)

2. 가까운 다른 땅 찾기 - 모든 땅 경계노드에서 다른 땅으로의 최소거리를 찾고 그 중 최소를 답으로 출력
- 전체를 돈다
- 땅(1)이 나오면 주변에 바다(0)가 있는지 확인
    - 없으면 패스함
    - 바다가 있으면 바다를 거쳐 가장 가까운 다른 땅을 찾아야 함
    - 바다의 주변노드를 큐에 넣으며 탐색
        - 범위체크
        - 다음 노드로 가기 위해 거쳐온 바다 수가 현재까지 그 노드로 갔던 최소바다수(다리길이)보다 크거나 같으면 패스함
        - 바다가 나오면 큐에 넣고 해당 노드까지 거쳐온 최소바다수 갱신
        - 땅이 나오면 같은 땅인지 확인하고 다른 땅일 경우에만 최소다리길이 갱신
    - 거쳐온 바다 수가 현재까지의 최소바다수(다리길이)보다 크거나 같으면 패스함
- 모든 노드의 최소바다수 다시 0으로 초기화

좋아 일케 풀어보자!
'''

import sys
from collections import deque
input = sys.stdin.readline
INF = int(2e9)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dir_arr = [(0,1), (1,0), (-1,0), (0,-1)]


# 1. 섬 번호 붙이기
visited = [[False]*N for _ in range(N)]

grp_idx = 1 #2부터 시작
for i in range(N) :
    for j in range(N) :
        #1이 아닐 때 (=방문 전인 땅이 아닐 때)
        if board[i][j] != 1 :
            continue

        que = deque()
        grp_idx += 1
        que.append((i,j))

        #새로운 섬 bfs
        while que :
            x, y = que.pop()

            #섬 번호 표시
            board[x][y] = grp_idx

            for dir in dir_arr :
                nx, ny = x+dir[0], y+dir[1]

                #범위를 벗어나지 않고, 방문 전이며, 1일 때
                if 0 <= nx < N and 0 <= ny <N and not visited[nx][ny] and board[nx][ny]==1 :
                    visited[nx][ny] = True
                    que.append((nx,ny))

# print("\n")
# for line in board :
#     print(*line)


# 2. 가까운 땅 찾기
min_cnt = INF
min_cnt_arr = [[INF]*N for _ in range(N)] #칸 별로 최소이동횟수 기록 # TS 1 : bfs밖으로 옮김

for i in range(N) :
    for j in range(N) :
        grp = board[i][j]
        #물은 패스함
        if grp == 0 :
            continue
        
        que = deque()
        que.append((i, j)) #x, y
        min_cnt_arr[i][j] = 0

        while que :
            x, y = que.pop()
            cnt = min_cnt_arr[x][y]

            #이미 최적이 아닌 경우 패스
            if min_cnt <= cnt :
                continue

            for dir in dir_arr :
                nx, ny = x+dir[0], y+dir[1]

                #좌표 내이고, 최소이동횟수보다 적게 도달했다면 값을 확인
                if 0 <= nx < N and 0 <= ny < N and cnt+1 < min_cnt_arr[nx][ny] : # TS 2
                    nxt = board[nx][ny]

                    #같은 땅
                    if nxt == grp :
                        continue

                    #물
                    elif nxt == 0 :
                        min_cnt_arr[nx][ny] = cnt+1
                        que.append((nx, ny))
                        continue

                    #다른 땅 도착
                    else :
                        # print("arrive : (%d, %d)-(%d, %d) %d"%(i, j, nx, ny, cnt))
                        min_cnt = min(min_cnt, cnt) #다리 길이 최소값 갱신
                        continue
print(min_cnt)