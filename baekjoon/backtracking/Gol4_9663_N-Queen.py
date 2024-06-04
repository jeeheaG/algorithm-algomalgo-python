# v1 : 백트래킹
# TS : 2차원 좌표는 1차원 배열에 저장할 수도 있다.
# TIP : 리스트 인덱스도 함께 반복문 돌고 싶을 떈 enumerate(리스트)

'''
[문제해석]
N-Queen : 크기가 NxN인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
- N이 주어지고, N개를 놓을 수 있는 경우의 개수를 구하기
- 제한시간 : 10초 (뭐든 하라는 건가)
** 퀸은 가로세로대각선 어느방향으로든 원하는 만큼 이동할 수 있음
** 퀸 특성상 한 행에 여러개가 올 수 없으므로 NxN인 행에 N개를 두려면 무조건 각 행에 퀸이 한개씩 배치되어야 함

구상 3
- 배치한 퀸 좌표를 1차원 배열에 저장
- 체스판 좌표마다 이미 배치된 퀸 목록 돌며 배치 가능한 좌표인지 확인(좌표값으로 계산)
    - TS : 체스판 좌표를 다 돌지 않아도 됨. 퀸 특징때문에 어차피 한 줄에 하나밖에 못놔서 행변호만 반복문 돌면 된다..
        -> 무조건 한 행에 한 퀸 배치! 다음 퀸은 다음 행에서 탐색
            해당 행에 퀸을 하나도 배치할 수 없는 경우 N개를 배치할 수 없다는 의미이므로 백트래킹 할 것!
            -> 중복 없음
- 배치 가능하면 배치 후 dfs재귀
- 어디에도 배치 불가능하면 백트래킹
- n개 모두 배치했으면 경우의 수 +1
'''

N = int(input())

board = [-1]*N # x=인덱스, y=값에 좌표 저장
result = 0

def dfs(q_cnt) :
    if q_cnt == N :
        global result
        result += 1
        return
    
    i = q_cnt #현재 q_cnt개의 퀸이 이미 배치되어있으므로 q_cnt+1번째 행, 즉 인덱스 q_cnt인 행에 이번 퀸을 배치해야 함
    for j in range(N) : #이번 행의 열을 돈다
        # 퀸 목록 돌며 배치 가능한지 확인
        able = True
        for x, y in enumerate(board) :
            #배치 안 된 행은 확인하지 않고 패스
            if y == -1 :
                continue
            if i == x or j == y or abs(x-i) == abs(y-j) : #가로, 세로, 대각선 중 하나에 걸림
                able = False
        
        #이 열번호에 배치 불가. 다음 위치 탐색
        if not able :
            continue
        
        #배치 가능
        board[q_cnt] = j
        dfs(q_cnt+1)
        board[q_cnt] = -1

dfs(0)
            
print(result)


