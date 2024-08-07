# BJ CLASS 2

import sys
input = sys.stdin.readline

N = int(input())

people = []
for i in range(N) :
    age, name = input().split()
    people.append((int(age), i, name)) # 나이순 적용 후 입력순 적용

people.sort()

ans = []
for age, _, name in people :
    ans.append("%d %s"%(age, name))
print('\n'.join(ans))