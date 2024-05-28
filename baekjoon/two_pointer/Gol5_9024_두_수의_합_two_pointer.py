# v2 : 투 포인터
#직전에 푼 3273과 매우 유사한 문제!
#이진탐색 문제는 투 포인터로도 풀 수 있다!

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
- 3273번처럼 정렬 + 이진탐색 으로 짜면 될까? nlogn -> 이것도 파이썬은 시간초과. (pypy는 통과)
- 투 포인터로 풀어보자!
- 풀이
    - 투 포인터로, 시작점과 끝점에 포인터를 하나씩 두고 시작한다.
    - 두 수의 합res와 k의 갭이 그동안의 min_gap보다 작으면, min_gap갱신 & 조합수cnt초기화 후 +1 해준 뒤
        갭이 +이면 작은 쪽 포인터를 +1이동, 갭이 -이면 큰 쪽 포인터를 -1이동시켜 탐색을 이어서 진행한다.
        이때 갭이 0이면, 아무 포인터 하나만 1 이동 시키고 이어서 탐색한다.
    - 갭이 그동안의 min_gap과 같으면, cnt +1 해준 뒤
        앞선 경우와 동일하게 이어서 진행한다.
    - 갭이 그동안의 min_gap보다 크면, 다른 작업 없이
        앞선 경우와 동일하게 이어서 진행한다.
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
    #투 포인터 탐색
    left, right = 0, N-1
    while left < right :
        res = nums[left] + nums[right]

        gap = k - res
        gap_abs = abs(gap)

        #갭 차이에 따른 min_gap, cnt 처리
        if gap_abs < min_gap :
            min_gap = gap_abs
            cnt = 1
        elif gap_abs == min_gap :
            cnt += 1
        
        #갭의 부호에 따른 포인터 이동
        if gap <= 0 : 
            right -= 1 #현재 합이 k보다 큰 경우 큰 쪽 포인터를 -1 이동 (gap==0일 경우 아무 포인트 하나만 1 이동시키고 다음 탐색)
        elif 0 < gap :
            left += 1 #현재 합이 k보다 작은 경우 작은 쪽 포인터를 +1 이동
    
    print(cnt)