# BJ CLASS 2

import sys
input = sys.stdin.readline

answer = []

while True :
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[0]==0 and nums[1]==0 and nums[2]==0 :
        break

    answer.append("right" if nums[0]**2 + nums[1]**2 == nums[2]**2 else "wrong")

print("\n".join(answer))
