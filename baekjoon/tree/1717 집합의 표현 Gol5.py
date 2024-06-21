# v1 : union find +경로압축
# TS 1 : 합집합 연산 시 x,y가 포함된 집합 전체를 연결시켜야하므로 루트를 찾아서 연결해야 함!
# TS 2 : 시간초과(pypy도)
#   1. 합집합 시 항상 한쪽 루트노드의 자식으로 연결함
#   2. find연산 재귀로 변경
#   3. find연산 시 최적화 - 경로압축 적용!
#   경로압축까지 적용해서 시간초과 해결할 수 있었다..~ 파이썬은 최적화가 생명이군아

'''
[문제 해셕]
0~n 각 하나씩만 원소로 갖는 집합 n+1개가 주어지고, 이들 간의 집합 연산 결과 출력하기
- 0 a b : a와 b가 포함되어있는 집합의 합집합 연산
- 1 a b : a와 b가 같은 집합의 원소인지 확인하는 연산
    - a = b 일 수도 있음
- 1 <= n <= 1000000
- 1 <= 연산개수m <= 100000
- 시간제한 : 2초
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

# i번 인덱스에 원소 i의 부모노드를 기록해둔 배열. 원소가 루트노드일 경우 자기자신을 기록
parent_arr = [i for i in range(N+1)] #0~n

# x, y가 포함된 집합의 합집합 연산 메서드
def union(x, y) :
        if x==y :
             return
        # parent_arr[find(y)] = x # TS 1 : y의 루트노드를 x의 자식으로 연결함
        parent_arr[find(y)] = find(x) # TS 2 : y의 루트노드를 x의 루트노드의 자식으로 연결함

# x의 루트노드 찾는 메서드 - 버전1
# def find(x) :
#     cur = x
#     while True :
#         parent = parent_arr[cur]

#         if parent == cur :
#             return parent
        
#         cur = parent

# x의 루트노드 찾는 메서드 - 버전2 재귀 # TS 2
# def find(x) :
#     if parent_arr[x] != x :
#         return find(parent_arr[x])
#     else : 
#         return x

# x의 루트노드 찾는 메서드 - 버전3 경로압축 # TS 2
def find(x) :
    if parent_arr[x] != x :
        parent_arr[x] = find(parent_arr[x]) #경로 압축!!
    return parent_arr[x]

for _ in range(M) :
    oper, x, y = map(int, input().split())
    if oper == 0 :
        union(x,y)
    else :
        print("YES" if find(x) == find(y) else "NO")