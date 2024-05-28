# v1 : 해시(딕셔너리)
#그냥 딕셔너리에 때려넣고 꺼내면 될 거 같은데..넴 됨

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}
for _ in range(N) :
    site, pw = input().split()
    dic[site] = pw

for _ in range(M) :
    site = input().strip()
    print(dic[site])