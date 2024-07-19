# v1 : 

'''
[문제해석]
보드 입력받아서
요구하는 값 출력해라?? 포인트가 뭐지
-> 그냥 구현했더니 시간초과 남. 뭘로 줄이는 거지?

- 시간제한 : 2초

'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
coms = [list(map(int, input().split())) for _ in range(K)]

ans = []
for com in coms :
    x, y, x_size, y_size = com
    x -= 1
    y -= 1

    x_end = x + x_size
    y_end = y + y_size

    b = board[x:x_end]
    res = 0
    for line in b :
        res += sum(line[y:y_end])
    ans.append(res)

    # print(x, x_end, y, y_end)
    # print(board[x:x_end])
    # ans.append(sum())

print('\n'.join(map(str, ans)))