# v1 : 힙


'''
[문제 해석]
- 시간대가 겹치는 수업들을 최소한의 강의실에 배치하라
- 답 : 강의실 최소개수
- 시간제한 : 1초



구상
일단 수업을 무조건 배치는 해야 됨
수업 시작시간, 종료시간을 시간순으로 정렬하고
시간을 흐르게 하면서 각 시간에 빈 강의실이 있다면 그걸 사용하고, 없다면 새로운 강의실을 추가하자
수업이 끝나면 빈강의실+1
왜 힙이지? - 오 풀다보니까 알겠음..

=> heapq써도 시간초과
    -> 로직을 더 줄일 수 있을 듯? for문을 시간별로 안돌고
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

#시간을 돌면서 강의실 배정
for t in range(max(start)+1) : #제일 늦게 시작하는 강의의 시작시각까지 반복
    #남은 강의 중 제일 먼저 끝나는 강의가 현재시간과 같으면 계속 확인
    while end and end[0] == t : 
        heapq.heappop(end)
        using -= 1
        empty += 1

    #남은 강의 중 제일 먼저 시작하는 강의가 현재시간과 같으면 계속 확인
    while start and start[0] == t : 
        heapq.heappop(start)
        #빈강의실 있으면 그거줌
        if empty != 0 : 
            empty -= 1
        using += 1

#강의실 최소값 = 빈 강의실 수 + 현재 사용중인(끝나면 비게 될) 강의실 수
print(using + empty)
