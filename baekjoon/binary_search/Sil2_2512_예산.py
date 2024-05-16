# v1 : binary search
# 시간제한 : 1초 (연산 2천만20,000,000회 이내)
# TS : 상한액을 여러가지 따져가며 계산할 필요가 없음... 
#       그냥 이분탐색 원리 그대로 중간값으로 잡아서 계산해나가면 이분탐색 종료 후 최적의 상한액이 남게 됨ㅎㅎ.. 개념 숙지 부족이다
#       -> 이분탐색 시 left, right 가 꼭 인덱스일 필요는 없다

'''
[문제해석]
- 예산을 전부 배정 가능하면 그대로 ㄱ
- 예산이 넘치면 동일한 상한액 내에서 배정
- 답 : 배정된 예산 중 최댓값
'''

import sys
input = sys.stdin.readline # 기존 input대신 해당 함수로 대체

N = int(input())
req_arr = list(map(int, input().split()))
total = int(input())

answer = 0

#전부 가능한지
if sum(req_arr) <= total :
    answer = max(req_arr)

#넘치면 상한액 계산
else :
    #이진탐색 logN
    left, right = 0, max(req_arr)
    while left <= right :
        mid = (left + right) // 2
        
        give_total = 0
        for req in req_arr :
            give_total += min(req, mid)

        #배정 결과가 총예산 이내이면 갱신 후 더 큰 쪽을 탐색
        if give_total <= total :
            answer = mid
            left = mid + 1

        #총예산 넘쳤으면
        else : 
            right = mid - 1 #더 작은 쪽을 탐색

#배정 최댓값 출력
print(answer)