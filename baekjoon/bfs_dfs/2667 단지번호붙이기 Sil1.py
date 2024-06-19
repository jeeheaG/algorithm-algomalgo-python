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
- 칸 전체를 돈다
- visited면 넘어간다
- 방문 전이면서 1인 칸을 만나면 dfs
- 주변에 있는 1인 칸만 스택에 넣으며 dfs돈다 두두두
- 돌면서 1대신 그룹 번호로 바꿔준다 (0,1은 이미 입력데이터에서 사용중이므로 그룹 번호는 2부터 사용)
- dfs끝나면 칸 전체 돌기를 이어서 진행
'''

import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(N)] #strip()으로 개행문자 제거 후 문자열을 리스트로 만들어서 다시 map(int)씀
visited = [[False]*N for _ in range(N)]

dir_arr = [(0,1), (1,0), (-1,0), (0,-1)]
grp_size_arr = [0,0] #인덱스 2부터 사용할 것임

for i in range(N) :
    for j in range(N) :
        #이미 방문했던 칸이거나 1이 아니면 패스
        if visited[i][j] or board[i][j] != 1 :
            continue
            
        #방문 전이고, 1이면 새 그룹 dfs
        stack = []

        visited[i][j] = True
        stack.append((i,j))

        #새 그룹 세팅
        grp_size_arr.append(0)
        grp_idx = len(grp_size_arr)-1
        
        #dfs
        while stack :
            cur_i, cur_j = stack.pop()

            board[cur_i][cur_j] = grp_idx
            grp_size_arr[grp_idx] += 1

            #사방 칸 확인해서 1이면 스택에 넣음
            for dir in dir_arr :
                new_i, new_j = cur_i+dir[0], cur_j+dir[1]
                #범위 벗어나는지 확인 
                if new_i < 0 or new_j < 0 or N <= new_i or N <= new_j :
                    continue
                if visited[new_i][new_j] :
                    continue
                    
                visited[new_i][new_j] = True
                if board[new_i][new_j] == 1 :
                    stack.append((new_i, new_j))


print(len(grp_size_arr)-2) #그룹번호가 2부터 시작하니까
print('\n'.join(map(str, sorted(grp_size_arr[2:]))))