# v1 : 누적합

'''
[문제해석]
사람들이 순서대로 돈을 인출할 때 걸리는 시간의 총합 최소값 구하기. 사람마다 소요시간은 다름
-> 정렬하고 누적합

5
3 1 4 3 2

1 2 3 3 4 
작은 순으로 하면 최적

1 3 6 9 13 
이렇게 누적합구해서 다 더함
'''

import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))

times.sort()

# 누적합
for i in range(1, N) :
    times[i] += times[i-1]

print(sum(times))