# v1 : 힙(최대힙)
#파이썬은 그냥 heapq쓰면 되는 문제

'''
- 최대힙이므로 heapq쓸 때 값을 음수로 저장
- 입력된 자연수를 힙에 push
- 입력이 0이면 가장 큰 값을 pop (출력하고 그 값을 배열에서 제거)
'''

import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N) :
    oper = int(input())
    if oper == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            print(-1*heapq.heappop(heap))
    else :
        heapq.heappush(heap, -1*oper)
