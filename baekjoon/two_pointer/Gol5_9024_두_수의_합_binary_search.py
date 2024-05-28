# v1 : 정렬, 이진탐색
#직전에 푼 3273과 매우 유사한 문제!
# TS : 테케 통과, 시간초과.. pypy는 통과!!!
#       어떻게 시간을 더 줄이지?
#       -> 이진탐색 문제는 투 포인터로도 풀 수 있다!

'''
[문제 해석]
- 주어진 서로다른 수들 중 두 수의 합이 특정 수k에 가장 가까운 조합의 수
- 숫자들은 -10^8 ~ 10^8(1억) 사이 정수. 숫자의 개수n는 1,000,000개 이하
- 시간제한 : 1초
- 답 : 합이 k에 가장 가까운 두 수 조합의 개수

[예제]
10 4
-7 9 2 -4 12 1 5 -3 -2 0
정렬 -> [-7, -4, -3, -2, 0, 1, 2, 5, 9, 12]



구상
- 2천만 연산 내에 짜야 함. n^2이면 시간초과
- 3273번처럼 정렬 + 이진탐색 으로 짜면 될까? nlogn
- 탐색 풀이
    - 작은 쪽 수 하나 고정
    - 고정수보다 더 큰 쪽 범위 이진탐색
    - 두 수의 합res와 k의 갭이 그동안의 min_gap보다 작으면, min_gap갱신 & 조합수cnt초기화 후 +1 해준 뒤
        갭이 +인지 -인지에 따라 큰 쪽 수를 더 키울지 줄일지 정해 이진탐색 범위를 조정하여 이번 이진탐색을 이어서 진행한다.
        이때 갭이 0이면, 더 탐색하지 않는다.
    - 갭이 그동안의 min_gap과 같으면, cnt +1 해준 뒤
        앞선 경우와 동일하게 이진탐색 범위를 조정하여 이어서 진행한다.
    - 갭이 그동안의 min_gap보다 크면, 다른 작업 없이
        앞선 경우와 동일하게 이진탐색 범위를 조정하여 이어서 진행한다.
왜 골드이려나 . .
'''


import sys
input = sys.stdin.readline
INF = int(2e9)

T = int(input())
for _ in range(T) :
    N, k = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    min_gap = INF
    cnt = 0
    #완전 탐색
    for i in range(N) :
        #이진 탐색
        start, end = i+1, N-1
        while start <= end :
            mid = (start + end) // 2
            res = nums[i] + nums[mid]

            gap = k - res
            gap_abs = abs(gap)

            #갭 차이에 따른 min_gap, cnt 처리
            if gap_abs < min_gap :
                min_gap = gap_abs
                cnt = 1
            elif gap_abs == min_gap :
                cnt += 1
            
            #갭의 부호에 따른 이진탐색 범위 처리
            if gap < 0 : 
                end = mid - 1 #현재 합이 k보다 큰 것이므로 작은 쪽으로 범위 이동
            elif gap == 0:
                break #이진탐색 중지
            elif 0 < gap :
                start = mid + 1 #현재 합이 k보다 작은 것이므로 큰 쪽으로 범위 이동
    
    print(cnt)