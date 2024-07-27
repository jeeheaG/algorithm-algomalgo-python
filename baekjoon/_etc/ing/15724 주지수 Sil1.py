# v1 : dp(누적합)
# TS : 테케 잘 통과하는데 0%도 안가고 틀렸습니다
#       -> 솔루션보니까 논리는 맞는데.. board위에서 계산하지 말고 새로 dp테이블을 행, 열 하나씩 크게 0넣고 조건문 없이 짰음
#       -> 왜 이렇게 짜도 1% 틀렸습니다???

'''
[문제해석]
부분계산들이 중복됨
dp로 누적합을 계산해두고
요구하는 값 계산해 반환

- 시간제한 : 2초
- dp테이블 점화식 : dp[i][j] = dp[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
- 특정 구역합 계산할 때도 비슷한 방식
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]

#dp테이블 - TS : 이것도...
for i in range(1, N+1) :
    for j in range(1, M+1) :
        dp[i][j] = board[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

# print(*dp)

K = int(input())
coms = [list(map(int, input().split())) for _ in range(K)]

ans = []
for com in coms :
    x1, y1, x2, y2 = com
    ans.append(dp[x2][y2] - dp[x1][y1-1] - dp[x1-1][y1] + dp[x1-1][y1-1]) # 답 : 부분합 계산

print('\n'.join(map(str, ans)))




# dp테이블 -TS : 0없이 board에 그대로 짰는데 뭔가 범위 계산이 잘못된 듯..0넣고 다시짤래
# for i in range(N) :
#     for j in range(M) :
#         new = board[i][j]
#         if 0 < j :
#             new += board[i][j-1]
#         if 0 < i :
#             new += board[i-1][j]
#         if 0 < i and 0 < j :
#             new -= board[i-1][j-1]
        
#         board[i][j] = new
        

# K = int(input())
# coms = [list(map(int, input().split())) for _ in range(K)]

# ans = []
# for com in coms :
#     x1, y1, x2, y2 = com
#     res = board[x2-1][y2-1]
#     if 1 < x1 :
#         res -= board[x1-1][y1]
#     if 1 < y1 :
#         res -= board[x1][y1-1]
#     if 1 < x1 and 1 < y1 :
#         res += board[x1-1][y1-1]
    
#     ans.append(res)

# print('\n'.join(map(str, ans)))