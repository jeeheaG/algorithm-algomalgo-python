# BJ CLASS 2

import sys
input = sys.stdin.readline

N = int(input())

nums = [tuple(map(int, input().split())) for _ in range(N)]

result = []
for num in sorted(nums) :
    result.append('%d %d'%(num)) # 문자열로 변환

print('\n'.join(result))