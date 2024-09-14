# v1 : queue

'''
[문제 해석]
1초의 1개의 피자를 사람들에게 돌아가면서 나눠줄 때, 각 사람이 원하는 만큼 피자를 받을때까지의 시각 구하기
- 시간제한 : 2초

[구상]

예시
4
1 3 1 4

time = 0
(0,1) (1,2) (2,1) (3, 4) -> (사람 인덱스, 남은 피자)
그냥 시간 세고 남은 피자 차감하며 큐 돌리기
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))

que = deque()
for i in range(N) :
    que.append((i, people[i]))

ans = [0]*N
time = 0
while que :
    idx, need = que.popleft()
    time += 1

    if need == 1 :
        ans[idx] = time # 피자 다 받은 사람의 시간 기록
        continue

    que.append((idx, need-1)) # 원하는 피자 차감

print(*ans)