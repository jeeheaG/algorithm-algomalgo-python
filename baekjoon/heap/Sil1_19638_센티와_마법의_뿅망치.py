# v1 : 힙
# TS : 로직 돌리기 전과 후 모두 조건을 만족하는지 확인해줘야 하는 경우에 처리 주의하기!

'''
[문제 해석]
- 마법 뿅망치 : 키/2 가 됨. 키가 1일경우 영향x
- 항상 가장 키가 큰 사람 중 한명을 때림
- 때리는 횟수T 제한있음
- 답 : 모든 거인의 키가 센티의 키H보다 작게 할 수 있는가? 
    할 수 있다면 뿅망치 사용 최소횟수는?
    할 수 없다면 가능한 횟수만큼 다 때린 후에 가장 큰 거인의 키는?
- 시간제한 : 1초
- 거인의 수 N : N <= 10^5

- 최대힙이 필요하므로 heapq에 음수로 저장할 것
+ 문제에 안적혀있었는데, 키가 홀수일 경우 2로 나눈 몫으로 하면됨
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(2e9)

N, H, T = map(int, input().split())

heap = [-1*int(input()) for _ in range(N)]
heapq.heapify(heap)

#TS : 예외처리 - 이미 조건 만족함
if -1*heap[0] < H :
    print("YES\n0")
    sys.exit() #바로 실행 종료


#뿅망치 때리고 H보다 작아졌는지 확인
cnt = INF
for i in range(1, T+1) :
    h = -1*heapq.heappop(heap)
    new_h = h
    if h != 1 :
        new_h = h//2
    heapq.heappush(heap, -1*new_h)
    
    if -1*heap[0] < H :
        cnt = i
        break

#모두 작아지게 하기 실패 시
if cnt == INF :
    print("NO\n%d"%(-1*heap[0]))
#성공 시
else : 
    print("YES\n%d"%cnt)