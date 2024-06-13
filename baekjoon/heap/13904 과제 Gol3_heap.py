# v2 : 힙 (56ms)
#이 방식이 속도가 훨씬 빠르다!
#접근 방식을 아예 다르게 해야 힙을 쓸 수 있었다. 로직을 새로 짬. 더 효율적인 로직임!

'''
[문제 해석]
- 얻을 수 있는 점수 최댓값 구하기
- 과제는 하루에 1개만, 완료 시 점수
- 과제 별로 점수 다름. 마감일 지나면 점수x
- 과제 개수N <= 1,000 : 오 얼마 안되네?
- 마감일까지 남은 일수d <= 1,000
- 시간 제한 : 1초

구상 (힙 쓰는 ver)
- 과제 점수 기준으로 최대힙을 만든다.
- 점수가 가장 큰 과제부터 힙에서 pop하며 해당 과제 마감일에 배치해본다.
- 해당 날짜에 이미 배치가 되어있으면 배치 가능한 날짜 중 마감일 이전 가장 늦은 날짜에 배치한다. 
이러면 어차피 점수가 큰 순이라 최적이 된다! 무조건 점수 큰 걸 먼저 배치해야 유리하니까.. 오.. 나는 생각 못한 방식이다
'''

import heapq
import sys
input = sys.stdin.readline

N = int(input())
works = []
max_day = 0
for _ in range(N) :
    day, score = map(int, input().split())
    works.append((-1*score, day)) #heapq를 최대힙으로 쓰기위해 음수로 저장

    max_day = max(max_day, day) #가장 늦은 마감일 저장

heapq.heapify(works)

score_arr = [0]*(max_day+1)
while works :
    score, deadline = heapq.heappop(works) #가장 점수가 높은 과제
    score *= -1 
    # print(deadline, score)
    for day in range(deadline, 0, -1) :
        # print(day)
        if score_arr[day] == 0 :
            # print("set")
            score_arr[day] = score
            break

# print(score_arr)
print(sum(score_arr))
    