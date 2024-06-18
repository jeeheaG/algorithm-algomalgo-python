# v1 : dfs

'''
[문제 해석]
연결된 그룹의 수와 크기를 세는 문제
- 가로세로로 인접되어있으면 같은 그룹임
- 각 그룹마다 번호 붙임
- 각 그룹마다 몇개가 포함되어있는지 개수 셈
- 시간제한 1초
- 5 <= N <= 25

구상
visited 전인 칸 전체를 돈다
1이면 주변에 있는 1인 칸을 스택에 넣으며 dfs돈다 두두두
'''

import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(N)] #strip()으로 개행문자 제거 후 문자열을 리스트로 만들어서 다시 map(int)씀
visited = [[False]*N for _ in range(N)]

print(board)

dir_arr = [(0,1), (1,0), (-1,0), (0,-1)]
grp_idx = 1
grp_size_arr = [0,0] #인덱스 2부터 사용할 것임

for i in range(N) :
    for j in range(N) :
        #이미 방문했던 칸이거나 0이면 pass
        if visited[i][j] or board[i][j] == 0 :
            continue

        stack = []
        stack.append((i,j))
        
        while stack :
            cur_i, cur_j = stack.pop()

            # 1이면 사방 칸 확인해서 1이면 스택에 넣음
            if board[i][j] == 1 :
                for dir in dir_arr :
                    new_i, new_j = i+dir[0], j+dir[1]
                    #범위 벗어나는지 확인 
                    if new_i < 0 or new_j < 0 or N <= new_i or N <= new_j :
                        continue

                    nxt = board[new_i][new_j]

                    #같은 그룹
                    if nxt == 1 :
                        stack.append((new_i,new_j))
            
            
# 으아아 다시 생각


print(grp_idx)
print(grp_size_arr)

print(board)