# v1 : dp
#       - 점화식 : dp[alp][cop] = min(dp[alp-1][cop]+1, dp[alp][cop-1]+1, 문제를 풀어서 도달시켜둔 값)
#       - dp는 과거 계산결과를 사용한다 = 앞에걸 먼저 업데이트해둬도 됨..!!!...!!
# TS 1 : 인덱싱할 때 꼭꼭 범위체크 생각해주기...
# TS 2 : 런타임에러??? -> alp, cop 초기값이 처음부터 목표값보다 클 경우 처리..

# [문제 해석]
# 최단기간 안에 목표 알고력, 코딩력에 도달하기
# problem = [필알, 필코, 증알, 증코, 시간]
# 문제안풀고는 시간 1에 1씩 증가

INF = int(2e9)

def solution(alp, cop, problems):

    #목표 알고, 코딩력 구하기
    max_alp, max_cop = 0, 0
    for problem in problems :
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])

    # TS 2 : 예외케이스 처리!!!! 
    #alp, cop 초기값이 처음부터 목표값보다 클 경우 : 인덱싱에러 나지 않게 목표값으로 만들어버림
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    #dp[alp][cop] = alp, cop 에 도달하려면 걸리는 최단시간
    dp = [[INF]*(max_cop+1) for _ in range(max_alp+1)]
    #현재 alp, cop까지의 도달시간 업데이트
    dp[alp][cop] = 0

    #dp테이블을 돈다
    for i in range(alp, max_alp+1) :
        for j in range(cop, max_cop+1) :
            #alp 또는 cop를 1씩 증가시키는 것과 현재값 중 더 작은 것으로 업데이트
            if 0 < i :
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j])
            if 0 < j :
                dp[i][j] = min(dp[i][j-1]+1, dp[i][j])
                

            #현재 alp, cop 에서 풀 수 있는 문제를 풀었을 때 도달할 수 있는 dp값들 업데이트해둠
            for problem in problems :
                alp_req, cop_req, alp_get, cop_get, cost = problem

                #못 푸는 문제면 넘어감
                if i < alp_req or j < cop_req :
                    continue

                #풀 수 있다면 풀었을 때 도달할 수 있는 시간을 dp테이블에 원래값과 비교하여 업데이트
                new_alp = min(i + alp_get, max_alp) #얻은 alp, cop가 목표값을 넘어도 목표값에 저장해줘야 함
                new_cop = min(j + cop_get, max_cop)
                dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)

    return dp[max_alp][max_cop]


# 테스트
print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]])) #15
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])) #13