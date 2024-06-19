# v1 : bfs
#직전에 푼 1697과 유사

'''
[문제 해석]
1697 숨바꼭질 문제와 동일하나, 2배 이동을 하는 경우 드는 시간이 0이라는 점만 다르다.
- N에서 K로 가는 가장 빠른 횟수 찾기
- 한 횟수에 할 수 있는 이동의 종류는 3가지
    1. +1
    2. -1
    3. 2배
- 0 ≤ N, K ≤ 100,000
- 시간제한 2초
- 메모리제한 512 MB

구상
- 매번 세가지 경우 모두 bfs 돈다
- 단, 아래 조건을 만족하지 않으면 큐에 넣지 않는다.
    - 이미 방문했던 숫자의 경우 이전의 해당 숫자까지 갔던 최소이동횟수보다 클 때
    - 숫자가 이동 가능 범위를 벗어날 때 (0 ≤ N ≤ 100,000)
    - 이동 횟수가 현재까지의 최소이동횟수보다 클 때
- 2배 이동을 하는 경우 이동횟수+1을 하지 않는다.
'''

import sys
from collections import deque
input = sys.stdin.readline
INF = int(2e9)

N, K = map(int, input().split())

que = deque()

que.append((N, 0)) #현재위치, 이동횟수
min_cnt_arr = [INF]*100001 #모든 숫자의 최소이동횟수를 기록해둠

while que : 
    cur, cnt = que.popleft()

    #도착점까지의 최소이동횟수 또는 현재지점까지의 최소이동횟수보다 이동횟수가 큼
    if min_cnt_arr[K] <= cnt or min_cnt_arr[cur] <= cnt :
        continue

    min_cnt_arr[cur] = cnt #cur == K 인 경우의 정답 업데이트가 포함됨

    for nxt in [cur+1, cur-1, cur*2] :
        if 0 <= nxt <= 100000 :
            new_cnt = cnt if nxt == cur*2 else cnt + 1
            que.append((nxt, new_cnt))

print(min_cnt_arr[K])