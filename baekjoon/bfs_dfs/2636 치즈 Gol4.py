# v1 : bfs

'''
[문제 해석]
치즈의 공기에 노출된 부분이 한시간에 한칸씩 녹을때, 마지막에 녹은 치즈 칸수와 다 녹기까지 걸린 시간은?

-> BFS로 공기를 상하좌우 인접한 것만 탐색해나가면 치즈 속 구멍을 공기로 인식하지 않도록 처리가 가능해짐!

구상
1. 전체 치즈 개수 적어둠
2. BFS 돌며 공기랑 인접한(이번에 녹을) 치즈 위치 적어둠
3. 녹임. 녹은 치즈 개수를 전체 치즈 개수에서 빼서 남은 치즈 개수 계산해둠
4. 다 녹을 때까지 반복
'''

from collections import deque
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

# 전체 치즈 개수 세놓기
cheeze_cnt = 0
for line in board : 
    for v in line :
        if v == 1 :
            cheeze_cnt += 1

print(cheeze_cnt)

dir_arr = [(1,0), (0,1), (-1,0), (0,-1)]
que = deque()

time = 0
last_cheeze_cnt = 0
while cheeze_cnt :
    time += 1

    visited = [[False]*w for _ in range(h)]
    que.append((0,0)) # 공기 전부 탐색
    visited[0][0] == True
    melt = []

    while que :
        x,y = que.pop()
        
        for dir in dir_arr :
            nx = x + dir[0]
            ny = y + dir[1]

            # 0이면 공기 bfs 탐색에 넣고 1이면 녹을 치즈로 추가
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] :
                visited[nx][ny] = True
                if board[nx][ny] == 0 :
                    que.append((nx, ny))
                else :
                    melt.append((nx, ny))

    # 치즈 녹이기
    last_cheeze_cnt = cheeze_cnt
    cheeze_cnt -= len(melt)

    for i, j in melt :
        board[i][j] = 0

print(time)
print(last_cheeze_cnt)
