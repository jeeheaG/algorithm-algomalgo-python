# BJ CLASS 2

import sys
input = sys.stdin.readline

nums = []

N = int(input())

for _ in range(N) :
    n = int(input())
    if n == 0 :
        nums.pop()
    else :
        nums.append(n)

print(sum(nums))