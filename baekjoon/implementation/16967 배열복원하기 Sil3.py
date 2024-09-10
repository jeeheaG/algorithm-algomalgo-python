# v1 : 구현

'''
[문제 해석]
- 배열을 겹쳐두고 겹친 영역은 값을 더한 결과를 적어두었을 때, 원래 배열 구하기
- 시간제한 : 2초


[구상 with 예시]
H W X Y
3 3 2 1

2-1 = 1
1-1 = 0
-> 행 1, 열 0 까지만 원래 배열
-> 나머지는 (i,j) - (i-X, j-Y) 원래값 계산 해서 넣어줘야 함

    0 1  2 3
------------
0 | 1 2  3 0
1 | 4 5  6 0
2 | 7 9 11 3
3 | 0 4  5 6
4 | 0 7  8 9

'''

import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(H+X)]

real = [[0]*W for _ in range(H)] # 실제 배열을 담을 list

for i in range(H) :
    for j in range(W) :
        if i < X or j < Y :
            real[i][j] = board[i][j]
            continue
        
        # 겹치는 구간은 (i,j) - (i-X, j-Y) 원래값 계산 해서 넣어줘야 함
        real[i][j] = board[i][j] - real[i-X][j-Y]


# 출력
for line in real :
    print(*line)