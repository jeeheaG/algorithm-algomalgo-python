# v1 : greedy
#전에 풀었던 14698 슬라임문제랑 비슷함

'''
[문제 해석]
모든 카드를 합치는 비교 횟수 최솟값
정렬된 카드묶음들이 주어짐
카드 묶음은 두개씩 합칠 수 있고, 합칠때에는 두 묶음의 카드수 합만큼 비교가 필요함

구상
전에 풀었던 슬라임문제랑 비슷하네?
작은묶음부터 합치면 될 듯
새로 생긴 묶음을 포함해 다시 정렬해야 하므로 정렬 상태를 유지하면서 삽입삭제가 필요함 -> 힙(우선순위큐)
'''

import sys, heapq
input = sys.stdin.readline

N = int(input())

cards = [int(input()) for _ in range(N)]

heapq.heapify(cards)

add_sum = 0
while 1 < len(cards) :
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)

    add = c1+c2
    add_sum += add
    heapq.heappush(cards, add)

print(add_sum)