# v1 : 구현

'''
[문제 해석]
주어진 구름이 계속 동쪽으로 한칸씩 이동할 때, H*W 짜리 보드에서 구역별 구름이 도착하는 시간


3 4
c..c
..c.
....

같은 행만 보면 됨
입력 다 받고 돌면서 값바꾸기
'''

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = [list(input().strip()) for _ in range(H)]

for i in range(H) :
    from_cloud = -1
    for j in range(W) :
        cloud = board[i][j]
        if cloud == 'c' :
            from_cloud = 0
        board[i][j] = from_cloud

        if from_cloud != -1 :
            from_cloud += 1

for line in board :
    print(*line)