# BJ CLASS 2

import sys
input = sys.stdin.readline

N = int(input())

nums = [tuple(map(int, input().split())) for _ in range(N)]

nums.sort(key = lambda x : (x[1], x[0]))

for num in nums :
    print(*num)