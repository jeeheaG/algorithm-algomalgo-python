# v1 : 그냥 구현함 (112ms)
#로직 특성상 힙을 활용한 방식보다 느리다.

'''
[문제 해석]
- 얻을 수 있는 점수 최댓값 구하기
- 과제는 하루에 1개만, 완료 시 점수
- 과제 별로 점수 다름. 마감일 지나면 점수x
- 과제 개수N <= 1,000 : 오 얼마 안되네?
- 마감일까지 남은 일수d <= 1,000
- 시간 제한 : 1초

구상
- 과제를 마지막날부터 거꾸로 돌면서 배치하면 될 것 같다.
- 구현
    - 과제를 점수가 큰것부터 정렬
    - 날짜를 거꾸로 돌면서, 해당 날짜에 마감일이 아직 지나지 않은 과제 중 가장 점수가 높은 과제를 해당 날짜에 배치
        - 이 부분 구현 방법 생각나는 거 2가지
            1. 점수 기준으로 정렬하고, 점수 제일 큰 과제에서부터 날짜가 지났는지 확인. 날짜가 안지난 게 나오면 바로 pop (리스트pop이라 시간많이 걸릴듯)
            2. 날짜 기준으로 정렬하고, 날짜가 아직 안지난 과제까지만 돌면서 점수들 중 최대값 갱신하면서 구함
                - 최악의 경우 nlogn + d*n = d*n (n^2) 인데 최악이라도 n, d가 1000밖에 안돼서 1000^2 = 10*6 < 10^8 이라 괜찮을 거 같은... 해볼까
                -> 이걸로 풀었는데 성공했다. 힙 쓰는 풀이도 찾아봐야지
'''


import sys
input = sys.stdin.readline

N = int(input())
works = [tuple(map(int, input().split())) for _ in range(N)]
done = [False]*N

works.sort(reverse=True) # 튜플 첫번째 값인 날짜가 큰 기준으로 정렬됨

score_sum = 0
for day in range(works[0][0], 0, -1) : #가장 큰 마감일부터 날짜를 돈다

    score_max_idx = -1
    score_max = 0
    for i in range(len(works)) :
        deadline, score = works[i]

        #마감일 지난 과제가 나왔으면 이번 날짜 탐색 중지
        if deadline < day :
            break
        #이미 한 과제면 넘어감
        if done[i] :
            continue
        
        #점수 더 높은 과제가 나왔으면 갱신. 이때 점수가 동일해도 마감일이 늦은 걸 골라야 유리하므로 등호 미포함
        if score_max < score :
            score_max_idx = i
            score_max = score


    #아무 과제도 선택되지 않았으면 넘어감
    if score_max_idx == -1 :
        continue

    #최종적으로 이 날짜에 선택된 과제 완료 처리, 점수 증가
    done[score_max_idx] = True
    score_sum += score_max

print(score_sum)
    