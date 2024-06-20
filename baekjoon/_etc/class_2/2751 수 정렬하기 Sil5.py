# BJ CLASS 2

import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(int(input()))]

print('\n'.join(map(str, sorted(nums))))