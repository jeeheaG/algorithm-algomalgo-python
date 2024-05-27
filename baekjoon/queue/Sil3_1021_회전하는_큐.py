# v1 : 큐
#원형, 양방향 큐 -> deque!!!!

'''
[문제 해석]
- 가능한 연산 3가지
    1. 첫번째 원소 추출 : 인덱스 1번 원소 사라짐 (인덱스 1부터 시작)
    2. 왼쪽 회전    : 인덱스값 i+1
    3. 오른쪽 회전  : 인덱스값 i-1
- 원소는 주어진 순서대로 뽑아야 함
답 : 원하는 원소를 뽑아내기 위한 최소 회전연산 횟수

[구상]
문제 이해가 잘 안돼서 솔루션 봤는데
원소가 뽑히면 맨 앞에서부터 1로 새로 인덱싱이 되는 거고
뽑아낼 수 있는 건 항상 맨 앞 원소인 것.
설마 진짜로 직접 원소 옮겨주는 건지 생각 안하고
인덱스 갖고 놀거나 큐는 가만있고 포인터 하나 왔다갔다 하는 건줄 알았는데
deque가 있었다.. 양방향 큐에 직접 양쪽 넣다뺐다 해주면 된다

-> 어차피 순서대로 뽑아야 하니까, 
    deque쓰고 
    현재 인덱스를 왼쪽/오른쪽 중 어디로 돌려야 1번 자리로 빨리 가져올 수 있는지만 판단해서 회전횟수 세면 됨
'''

from collections import deque
import sys
input = sys.stdin.readline

max_size, N = map(int, input().split())
want_idx_arr = list(map(int, input().split()))

que = deque(range(1, max_size+1)) #데크에 초기 인덱스값인 1~N를 담음

turn_cnt = 0 #회전횟수
for want_idx in want_idx_arr :
    #맨 앞 원소가 뽑으려는 원소이면 뽑고 패스
    if que[0] == want_idx :
        que.popleft()
        # print("%d 바로 뽑음 : %d"%(want_idx, que.popleft()))
        continue

    #뽑으려는 원소가 아니면 돌리고 뽑음
    que_size = len(que)
    for i in range(que_size) :
        if que[i] == want_idx :
            turn = 0
            #오른쪽으로 돌리는 게 빠름 (인덱스 작아지는 쪽)
            if i <= que_size//2 :
                turn = i
                for _ in range(turn) :
                    que.append(que.popleft())
            #왼쪽으로 돌리는 게 빠름 (인덱스 커지는 쪽)
            else :
                turn = que_size - i
                for _ in range(turn) :
                    que.appendleft(que.pop())
            turn_cnt += turn
    que.popleft()
    # print("%d번 돌려서 %d 뽑음 : %d"%(turn, want_idx, que.popleft()))

print(turn_cnt)
