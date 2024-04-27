# v1 : bfs
# bfs로 풀어보자 bfs면 더 깊은 노드까지 내려간 게 더 낮은 점수를 맞춘 결과일테니 그걸 반환하도록 해보자
# https://school.programmers.co.kr/learn/courses/30/lessons/92342
# ISSUE 1 : 트리의 끝일 경우 처리
# ISSUE 2 : 안맞추는 경우를 나중에 추가해야 함. 그래야 낮은 점수를 맞춘 경우가 최종 답으로 남음!!
# ISSUE 3 : 안맞추는 경우를 나중에 추가하므로 안맞추는 경우에 사용할 board를 살려놨어야 함
# ISSUE 4 : 점수조건 충족했는데 화살이 남은 경우는 남은 걸 모두 0에다 쏴서 화살을 버리도록 해야 함. 더 낮은 점수를 맞춘 경우로 만들어야 하므로.
# ISSUE 5 : 테스트케이스 8, 18 fail : 화살이 남았을 경우만 다음 점수판을 계속 탐색하게 해야 함! 화살이 없는데도 다음 탐색을 큐에 넣으면 더 낮은 점수를 맞춘 경우로 인식해서 오답이 나옴


from collections import deque

def solution(n, info):
    answer = []

    scores = [] #(cost, score)
    rival_score = 0 #어피치 점수 계산할 변수

    for i in range(len(info)) :
        info_score = 10-i
        if info[i] == 0 :
            scores.append((1, info_score))
        else :
            scores.append((info[i]+1, info_score*2))
            rival_score += info_score #어피치 점수 계산

    que = deque()
    que.append((0, 0, 0, [0]*11))
    max_gap = 0 # 점수차 최대값

    while que :
        cost, score, depth, board = que.popleft() #현재까지의 사용화살 수, 누적점수, 그래프 깊이, 쏜 화살 결과를 담은 보드

        #이기는 조건을 만족하고, 점수 차가 더 크면
        if cost <= n and rival_score < score :
            gap = score-rival_score
            if max_gap <= gap : 
                max_gap = gap
                # 화살이 남았다면 남은 걸 다 0에다 쏘게 처리
                if cost < n :
                    temp_board = board.copy()
                    temp_board[-1] = n - cost
                    answer = temp_board.copy()
                else : 
                    answer = board.copy()

        #트리의 끝이라면 
        if depth == len(info) : #11
            continue

        #다음 점수판을 맞출 수 있는 경우 : 맞춤
        next_cost = cost+scores[depth][0]
        if next_cost <= n  :
            temp_board = board.copy() #안맞추는 경우의 board를 살려놔야 함
            temp_board[depth] = scores[depth][0] #화살 쏜 거 반영
            que.append((next_cost, score+scores[depth][1], depth+1, temp_board))
        #화살이 남았지만 다음 점수판을 안맞추는 경우 : 현상유지해서 다음 깊이 탐색
        if cost < n :
            que.append((cost, score, depth+1, board.copy()))

    #못 이길 경우 -1 반환
    if max_gap == 0 :
        return [-1]
    return answer


# 테스트
# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) #[0,2,2,0,1,0,0,0,0,0,0]
# print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])) #[1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]
# print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3])) #[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]
print(solution(3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1])) #[1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]

