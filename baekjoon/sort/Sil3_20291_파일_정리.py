# v1 : 정렬? 파이썬은 다 해주는 걸?...

'''
[문제 해석]
- 확장자 별 개수 카운트
- 확장자 개수 출력 시 사전순 정렬
'''

from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
name_cnt = defaultdict(int)

file_arr = [input().strip().split(".")[1] for _ in range(N)]

#개수세기
for file in file_arr :
    name_cnt[file] += 1

#확장자 목록 만들어서 사전순 정렬
name_arr = []
for name, cnt in name_cnt.items() :
    name_arr.append(name)
name_arr.sort()

#출력
for name in name_arr :
    print(name, name_cnt[name])