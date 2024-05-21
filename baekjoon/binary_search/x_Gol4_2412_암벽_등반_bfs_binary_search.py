# pause : bfs 구현코드에 이진탐색을 추가로 사용해서 풀어보.. 려고 했으나 관둠
# main idea는 bfs최소경로찾기, 거기에 이진탐색을 쓰면 시간을 더 줄일 수 있음
# 이게 왜 이진탐색???
#   -> 이진탐색 안써도 풀리는 문제ㅇㅇ
#   -> 최소거리 찾는 거 자체는 bfs 해주면 되는데, 간선 데이터가 주어지지 않아서 간선찾기에 이진탐색을 쓸 수 있음
#        이진탐색 : 홈을 정렬하고, 이진탐색으로 현위치에서 이동 가능한 최소&최대 홈을 구한다. 그 후 정렬된 홈 목록에서 최소&최대 홈 사이의 홈들만 탐색하도록 한다!.
# PS. 이진탐색으로 푸는 걸 그다지 추천하지 않는 문제라고 한다.. 그냥 set에 넣으면 됨
# TS : 아니 x랑 y중에 무슨 근거로 하나만 잡아서 이분탐색을 한다는 거지??? 나 진짜 몰르겠

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
hole_arr = []
for _ in range(n) :
    hole_arr.append(tuple(map(int, input().split())))

hole_arr.sort()

que = deque()
que.append((0, 0, 0)) # x, y, cost
visited = set() #방문한 노드들 담는 조합
visited.add((0, 0))

#bfs
min_cost = INF
while que :
    x, y, cost = que.popleft()

    #도착했으면 최소값 갱신
    if T <= y :
        min_cost = min(min_cost, cost)
        continue

    #도착 전이면 다음 노드 탐색 - 다음 노드를 이진탐색
    #조건을 만족하는 최적(최소&최대)의 노드를 찾기
    #조건 : 현재 노드에서 차이 2이하
    min_hole, max_hole = (0,0), (0,0)

    #이진탐색 : 최소 홀 찾기
    #노드 중 좌표차가 2이하이고 x값이 가장 작은 노드 찾기
    idx_l, idx_r = 0, n
    while idx_l <= idx_r :
        mid = (idx_l + idx_r) // 2
        
        hole = hole_arr[mid]
        if -2 <= dist(hole) =< 2 :

        elif dist(hole) < -2 :
            idx_l
            
        elif 2 < dist(hole) :



    #이진탐색 : 최대 홀 찾기
    #노드 중 좌표차가 2이하이고 x값이 가장 큰 노드 찾기
    idx_l, idx_r = 0, n
    while idx_l <= idx_r :
        mid = (idx_l + idx_r) // 2
    


    #찾은 최소&최대 노드 범위 내의 모든 노드를 큐에 넣어 탐색함

    


#목적지에 도착할 수 없는 경우
min_cost = -1 if min_cost == INF else min_cost

print(min_cost)