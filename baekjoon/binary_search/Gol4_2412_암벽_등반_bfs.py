# v1 : 일단 bfs로만 풀어봄
# main idea는 bfs최소경로찾기, 거기에 이진탐색을 쓰면 시간을 더 줄일 수 있음
# 이게 왜 이진탐색???
#   -> 이진탐색 안써도 풀리는 문제ㅇㅇ
#   -> 최소거리 찾는 거 자체는 bfs 해주면 되는데, 간선 데이터가 주어지지 않아서 간선(현위치에서 이동 가능한 홈)찾기에 이진탐색을 쓸 수 있음
# TS : 시간초과
#       1. 다음 노드를 찾을 때 노드를 모두 확인하는 게 아니라 원하는 숫자 범위 안에 노드가 존재하는지 탐색하는 게 더 빠르다..!! 오
#       2. set사용 : in 연산 시 list 보다 set이 빠름


'''
[문제해석]
- 홈에서 x,y좌표의 차이가 모두 2이하인 지점으로 이동 가능
- (0,0)에서 정상 (_, T)까지 이동
- 이동 횟수를 최소로

답 : 최소 이동 회수
'''

from collections import deque
import sys
input = sys.stdin.readline
INF = int(2e9)

n, T = map(int, input().split())
hole_arr = set()
for _ in range(n) :
    hole_arr.add(tuple(map(int, input().split())))

que = deque()
que.append((0, 0, 0)) # x, y, cost
visited = set() #방문한 노드들 담는 배열
visited.add((0, 0))

#bfs
min_cost = INF
while que :
    x, y, cost = que.popleft()

    #도착했으면 최소값 갱신
    if T <= y :
        min_cost = min(min_cost, cost)
        continue

    #도착 전이면 다음 노드 탐색 - x,y좌표의 차이가 2이하인 범위 내에 노드가 존재하면 탐색
    for hx in range(x-2, x+3) :
        for hy in range(y-2, y+3) :
            if (hx, hy) in hole_arr and (hx, hy) not in visited:
                que.append((hx, hy, cost+1))
                visited.add((hx, hy))


    # #도착 전이면 다음 노드 탐색 - x,y좌표의 차이가 2이하인 노드 탐색
    # for hole in hole_arr :
    #     h_x, h_y = hole
    #     if abs(h_x - x) <= 2 and abs(h_y - y) <= 2 :
    #         if hole not in visited :
    #             que.append((h_x, h_y, cost+1))
    #             visited.add((h_x, h_y))

#목적지에 도착할 수 없는 경우
min_cost = -1 if min_cost == INF else min_cost

print(min_cost)