# v1 : 누적합
# TS : 음수일 수 있는 최대값 구할 때 초기화 숫자 0안됨~

'''
[문제 해석]
연속적인 K일간의 온도의 합 중 가장 큰 값 구하기
- 시간제한 : 1초

누적합 구해서 부분합으로 계산하면 빠를 것 같음

ex)
10 2
  3 -2 -4 -9   0  3  7  13  8 -3
0 3  1 -3 -12 -12 -9 -2 11 19 16
0    2                   8     10
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

nums = [0]
nums += map(int, input().split())

#누적합 구하기
for i in range(1, N+1) :
    nums[i] = nums[i-1] + nums[i]

#부분합 최대값 구하기
max_sum = -1 * int(2e9) # TS
for i in range(N-K+1) :
    max_sum = max(max_sum, nums[i+K] - nums[i])

print(max_sum)
