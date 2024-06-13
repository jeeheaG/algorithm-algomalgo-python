# v3 : 힙
# TS : 시간이 등장하는 문제에서 꼭 시각을 하나하나 돌려고 하지 말자. 유의미한 시각만 돌게 생각해볼 것

'''
[문제 해석]
- 시간대가 겹치는 수업들을 최소한의 강의실에 배치하라
- 답 : 강의실 최소개수
- 시간제한 : 1초



구상
수업 시작시각, 종료시각을 시간순으로 정렬하고
강의 시작 시각을 돌며 해당 시작 시각 전에 끝난 강의가 있는지 체크하여 빈강의실+1
빈 강의실이 있다면 그걸 사용하고, 없다면 새로운 강의실+1
왜 힙이지? - 오 풀다보니까 알겠음..

근데 다른 풀이들 보니까 힙 안쓰고도 구현 가능함
'''

import heapq
import sys
input = sys.stdin.readline

N = int(input())

start = []
end = []

for _ in range(N) :
    s, e = map(int, input().split())
    start.append(s)
    end.append(e)

#시간순 정렬 - heapq사용해서 최소힙으로 만듦
heapq.heapify(start)
heapq.heapify(end)

#현재 사용중인 & 비어있는 강의실 개수 저장 변수
using = 0
empty = 0

while start : #더 시작할 강의가 남아있을 때까지 반복
    #강의 시작 시각
    t = heapq.heappop(start)

    #시작시각 전에 끝난 강의가 있다면 강의실 반납
    while end and end[0] <= t :
        heapq.heappop(end)
        using -= 1
        empty += 1
    
    #강의실 배정
    if empty :
        empty -= 1
    using += 1

#강의실 최소값 = 빈 강의실 수 + 현재 사용중인(끝나면 비게 될) 강의실 수
print(using + empty)
