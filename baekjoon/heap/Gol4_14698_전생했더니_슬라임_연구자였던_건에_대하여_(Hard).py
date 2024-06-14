# v1 : 힙
# TS : 문제 잘못읽고 곱을 합으로 계산함 ㅎㅎ... 정신차리라

'''
[문제 해석]
- 슬라임을 2마리씩 합성하는데, 합성 시마다 두 슬라임의 에너지의 곱만큼 전기가 든다.
- 합성 결과로 두 슬라임의 에너지의 곱만큼의 에너지를 가진 한마리의 새로운 슬라임이 됨
- 슬라임을 모두 합성해 한마리로 만드는 데에 드는 모든 전기의 곱의 최소값
- 답 : 테스트케이스마다 모든 전기의 곱의 최솟값을 1, 000, 000, 007 로 나눈 나머지 출력

최소값을 어케 구할까..
-> 그냥 작은것부터 곱하면 된다고 한다 ㅎㅎ..ㅎ 왜지? 초반에 무조건 작게 가야해서 그런가
    가장 작은 슬라임 두개를 뽑아서 새 슬라임을 만들고, 바로바로 새로 생기는 슬라임을 포함해 최소값을 찾아야 하기 때문에 잦은 삽입삭제가 필요하다
    -> 힙을 써보자~~ heapq 최소힙 그대로 쓰면 됨
'''

import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    _ = int(input()) #슬라임 개수 안씀
    heap = list(map(int, input().split()))

    heapq.heapify(heap) #최소힙으로 만듦

    energy = 1
    while 1 < len(heap) :
        #가장 작은 슬라임 2개 pop
        s1 = heapq.heappop(heap)
        s2 = heapq.heappop(heap)

        result = s1*s2
        energy *= result #쓰인 모든 에너지들의 곱
        heapq.heappush(heap, result) #새로 생성된 슬라임 push
    
    print(energy%1000000007)