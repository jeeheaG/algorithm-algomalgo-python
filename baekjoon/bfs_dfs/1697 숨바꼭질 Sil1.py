# v1 : bfs
# TIP : dict, set보다 처음부터 초기화해서 쓰더라도 list가 더 메모리 적게 쓰고 빠를 수 있다.

# TS : 메모리 초과??? 
#   1. 방문했던 노드까지의 최소이동횟수를 모두 기록해두고 방문했던 노드이면서 최소이동횟수보다 많이 이동해서 도착한 경우라면 패스함
#   2. 이동 범위 제한 : 문제 조건 0 < N <= 1000000 가 움직일 수 있는 범위 자체를 제한한 거라고 한다
#       => 이게 핵심이었음.. 나머지는 그냥 겸사겸사
#   3. 1번 기록 시 메모리가 많이 드는 dict대신 list사용. 초기화 다 해줘도 list가 더 메모리 적게 쓰고 빠르다
#   (x) 메모리가 늘어날 부분은 que밖에 없어서 que에 append해주기 전에 조건을 검사하는 걸로 변경해봤다 -> 백준 채점에서 메모리 초과 더 빨리 떠서 안바꾸고 다시 돌려놓음

# Q : 아니 다들 visited체크를 해서 한번 방문한 노드는 다시 방문하지 않게 짜는데, 그게 왜 되지?? 더 최적으로 방문한 경로가 답이면 답이 걸러지지 않나

'''
[문제 해석]
- N에서 K로 가는 가장 빠른 횟수 찾기
- 한 횟수에 할 수 있는 이동의 종류는 3가지
    1. +1
    2. -1
    3. 2배
- 0 ≤ N, K ≤ 100,000 -> 이게 처음 주어지는 위치의 범위제한만 해당되는 걸로 이해했는데 이동할 수 있는 범위 자체가 저걸로 제한되어있다는 의미라고 한다
- 시간제한 2초
- 메모리제한 128 MB

구상
- 가장 빠른 경우를 어떻게 찾지 그냥 bfs로 다 돌아보는 건가
    각 경우마다 -1, +1, *2 이렇게 세가지 경우 다 해보는 걸로??
    그런가봐 중복만 잘 처리해서 짜보자 bfs
- 큐에서 pop
- 답인지 확인
- -1, +1, *2 한 값 중 직전값이 아닌걸 큐에 넣음
'''

from collections import deque
import sys
input = sys.stdin.readline
INF = int(2e9)

N, K = map(int, input().split())

que = deque()
que.append((N, 0)) #현재위치, 이동횟수

# min_move = dict() #방문했던 숫자의 최소이동횟수 기록
min_move = [INF]*1000001 #방문했던 숫자의 최소이동횟수 기록

min_cnt = INF

while que :
    cur, cnt = que.popleft()

    if min_cnt <= cnt :
        continue
    
    #정답
    if cur == K :
        min_cnt = cnt
        continue

    # if cur in min_move.keys() and min_move[cur] <= cnt :
    #     continue
    # min_move[cur] = cnt 

    #이전에 방문했던 최소이동횟수보다 많으면 탐색안함
    if min_move[cur] <= cnt :
        continue
    min_move[cur] = cnt

    for nxt in [cur+1, cur-1, cur*2] :
        if 0 <= nxt <= 1000000 : #TS
            que.append((nxt, cnt+1))

print(min_cnt)