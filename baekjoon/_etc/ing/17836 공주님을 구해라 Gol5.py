# pause : bfs
# TS 1 : 검이라는 변수가 있어서 bfs로 이미 방문했던 위치라도 더 짧은 시간에 다시 방문가능함. 최단 방문시간 적어두고 비교해줘야 함
# TS 2 : python 시간초과, pypy 메모리 초과.. -> 칼 찾았을 때 거리계산해서 하는 걸로 로직 바꿔서 시간 줄이기 성공
# TS 3 : 25% 틀렸습니다..

'''
[문제 해석]
T시간 내에 (n,m) 위치의 공주님 구하기
검을 찾으면 벽뚧고 감

구상
- 최단거리 bfs
- 검을 찾으면 벽뚫고 가기 시작 -> 이 부분을 달고다니면서 bfs로 하지말고 숫자계산으로 해야함
- 시간제한 1초
'''

from collections import deque
import sys
input = sys.stdin.readline
INF = int(2e9)

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dist_arr = [(1,0), (0,1), (-1,0), (0,-1)]

que = deque()
que.append((0, 0, 0)) # x좌표, y좌표, 소요시간, 검 획득 여부

# bfs
time = INF
while que :
    x, y, t = que.popleft()
    
    if T < t or time < t:
        continue # 이미 제한시간이나 최단시간 넘겼으면 패스
    
    #공주 도달 여부
    if x == N-1 and y == M-1 :
        time = min(time, t)
    
    for dist in dist_arr :
        nx = x + dist[0]
        ny = y + dist[1]

        # 범위 체크
        if nx<0 or N-1<nx or ny<0 or M-1<ny or visited[nx][ny] :
            continue

        # 칼 찾음 # TS 2
        if board[nx][ny] == 2 :
            t = t + 1 + (N-1-nx) + (M-1-ny)
            visited[nx][ny] = True
            que.append((N-1, M-1, t))
        # 칼 없이
        elif board[nx][ny] == 0 : 
            visited[nx][ny] = True
            que.append((nx, ny, t+1))

print("Fail" if time == INF else time) #time 이 갱신된 적 없으면 실패