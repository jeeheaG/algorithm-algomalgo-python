# TS : 이진탐색 범위는 중간값 안겹치게, left는 0부터..

'''
가능한 최대 예산 배정


- 모든 배정이 가능하면 그대로
- 모든게 불가하면 정수 상한액 계산 : 그 이상이면 상한액, 이하는 요청한 만큼만
- 배정된 예산 중 최대값 출력

4
120 110 140 150
485

1. 모두 배정 sum
2. 불가 시 상한액 계산 - 이진탐색으로 적정지점 찾기
3. 이하에는 이하만 배정하고, 넘치면 상한액을 배정할 수 있는 상한액 최대값
'''

import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())


# 상한선이 limit 일 때 총 배정액
def calTotal(limit) :
    s = 0
    for budget in budgets :
        s += min(budget, limit)
    return s


ans = 0
# 다 줄 수 있으면 다 주고 끝
if sum(budgets) <= M :
    ans =  max(budgets)

else :
    # 상한액limit 이진탐색 min~max

    l = 0 #TS
    r = max(budgets)

    while l <= r :
        mid = (l+r) // 2 # 상한액 후보

        total = calTotal(mid)
        if total < M : # 총예산 안이면 답 갱신, 인덱스 옮김
            ans = max(ans, mid)
            l = mid+1
        elif total == M :
            ans = mid # 배정안에 딱맞으면 더 탐색 안하고 바로 답 출력
            break
        else :
            r = mid-1

print(ans)