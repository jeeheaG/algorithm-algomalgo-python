# v1 : 힙

'''
자연수가 주어지면 삽입
0이 주어지면 가장 작은 수 pop
'''


import heapq
import sys
input = sys.stdin.readline

heap = []

def pop() :
    if heap :
        return heapq.heappop(heap)
    else :
        return 0 # heap이 비어있을 때 heappop을 호출하면 에러가 나므로 따로 처리 해줘야 함

for _ in range(int(input())) :
    oper = int(input())
    if oper == 0 :
        print(pop())
    else : 
        heapq.heappush(heap, oper)