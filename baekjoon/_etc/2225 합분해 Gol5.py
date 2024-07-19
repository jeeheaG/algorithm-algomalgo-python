# v1 : 

'''
[문제 해셕]
- 0~N 까지의 수 중 K개를 더한 값이 N이 되는 경우의 수
- 순서가 다르면 다른 것
- 중복 허용(한개의 수 여러번 사용 가능)
- 1 <= N, K <= 200
- 답 : 경우의 수를 1,000,000,000으로 나눈 나머지
- 시간제한 : 2초


dp??? 이걸 dp로 어케품??

아 완저니 수학이네..
문제를 수식적으로 작게 쪼갤 수 있는지 생각해보기

경우의 수를 적어놓은 dp테이블
dp[n][k] = n을 k개의 수로 나눈 경우의 수
dp[n][k] = dp[0][k-1] + dp[1][k-1] + ... + dp[n-1][k-1] + dp[n][k-1] 이고, 이를 한번 정리하면
dp[n][k] = dp[n-1][k] + dp[n][k-1]
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0]*(K+1) for _ in range(N)]

for i in range(N) :
    dp[i][1] = 1

answer = 0
def dfs(cur, cnt) :
    if cnt == K and cur == N :
        global answer
        answer += 1
        return
    
    new_cnt = cnt+1
    if K < new_cnt :
        return 
    
    for i in range(N+1) :
        new_cur = cur+i
        if N < new_cur :
            break
        dfs(new_cur, new_cnt)

    return answer

# 이번 경우의 수를 세주는 함수
def cal(n, k) :
    dfs(0, 0)
    return answer


for i in range(N) :
    for j in range(K+1) :
        dp[i][j] = dp[i-1][j-1] + cal(i, j-1) # dp[i][j-1]

