# pypy : 누적합
#pypy로만 통과한 코드

'''
[문제해석]
보드 입력받아서
요구하는 값 출력해라?? 포인트가 뭐지
-> 그냥 구현했더니 시간초과 남. 뭘로 줄이는 거지?

1 1 3 2 (1,1)위치부터 크기 3*2

보드를 그냥 사람수가 아니라
왼쪽부터 더해놓은 값으로 보드를 만들어놓음(누적합)
합 구할 때 행별로 부분합 구하는 계산만 함

행별로 말고 사각형으로 해야 python

- 시간제한 : 2초
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
coms = [list(map(int, input().split())) for _ in range(K)]

#행별 누적합으로 변경
for line in board :
    for j in range(1, M) :
        line[j] = line[j] + line[j-1]

ans = []
for com in coms :
    for i in range(4) :
        com[i] -= 1
    x, y, x_size, y_size = com
    
    # print(com)
    res = 0
    for line in board[x:x_size+1] :
        res += line[y_size] if 0 == y else line[y_size] - line[y-1]
    
    # print(res)
    ans.append(res)

print('\n'.join(map(str, ans)))