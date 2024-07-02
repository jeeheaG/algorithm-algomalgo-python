# v1 : greedy
# 어떤 걸 기준으로 할 지 아이디어만 떠올리면 쉬웠던 문제. 근데 난 못 떠올려서 솔루션봤다 ㅎ.ㅎ

'''
[문제 해석]
배치 가능한 회의의 최대 수 구하기
- 회의 시작시간과 끝나는 시간이 주어지며, 이는 같을 수도 있음
- 회의가 끝나자마자 시작 가능
- 시간은 24시간으로 분단위 없이 주어져서 편하게 쓰면 될듯~

구상
제일 많은 회의를 배치할 수 있는 경우는 ?
- 짧은 것부터? ㄴㄴ
- 빨리 시작? ㄴㄴ
- 겹치는 수 세두고 적은 거 > 짧은 거? ㄴ
-> 대박 끝나는 시간이래... 맞네
'''

import sys
input = sys.stdin.readline

N = int(input())

meets = []
for _ in range(N) :
    start, end = map(int, input().split())
    meets.append((end, start))

meets.sort()

cnt = 0
last_end = 0
for meet in meets :
    if last_end <= meet[1] :
        cnt += 1
        last_end = meet[0]

print(cnt)