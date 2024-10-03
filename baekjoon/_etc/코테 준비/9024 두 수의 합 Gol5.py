# TS : 포인터 옮기는 조건 잘 확인.. 차라리 손으로 그림 그려보기

'''
합이 K에 가장 가까운 두 정수 구하기

숫자 범위는 +-10^8

시간제한 : 1초
메모리 : 128

10 7
-7 9 2 -4 12 1 5 -3 -2 0
-7 -4 -3 -2 0 1 2 5 9 12

5
8
5
6
7

정렬해서 양쪽끝에서부터 한칸씩 옮기면 차이를 가장 작게 줄여갈 수 있음
'''

import sys
input = sys.stdin.readline

T = int(input())

ans = []
for _ in range(T) :
    n, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    l = 0
    r = n-1

    cnt = 0
    min_gap = int(2e9) # 이것보다 작으면 갱신하고 카운트 초기화, 이거랑 같으면 카운트, 이것보다 크면 버림
    while l < r :

        origin_gap = K - (nums[l] + nums[r])
        gap = abs(origin_gap)
        # print(nums[l], nums[r], gap)

        if gap < min_gap :
            min_gap = gap
            cnt = 1
        elif gap == min_gap :
            cnt += 1
        
        if origin_gap < 0 :
            r -= 1
        else :
            l += 1

    ans.append(cnt)

print("\n".join(map(str, ans)))