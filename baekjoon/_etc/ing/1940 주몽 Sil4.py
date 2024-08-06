# v1 : 투포인터
#그냥 list랑 set둘다 쓰면서 set에 in 연산자써서 푸는 방법도 된다고 한다!

'''
[문제 해석]
고유번호의 합이 M인 두 재료로 갑옷을 만들 수 있을 때, 주어진 재료들로 몇 개의 갑옷을 만들 수 있는가?
- 1 ≤ M ≤ 10,000,000
- 시간제한 : 2초

6
9
2 7 4 1 5 3
1 2 3 4 5 7

sort된 list를 M의 반까지만 돌면서 반대쪽 숫자 찾음
-> 투포인터
'''

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

nums = list(map(int, input().split()))
nums.sort()

cnt = 0

l = 0
r = len(nums)-1

while l < r :
    add = nums[l] + nums[r]
    if add == M :
        cnt += 1
        l += 1
        continue
    elif add < M :
        l += 1
        continue
    elif M < add :
        r -= 1
        continue

print(cnt)