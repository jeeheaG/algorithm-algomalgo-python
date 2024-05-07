# v1 : 큐 문제라는데 큐도 안쓰고 내맘대로 좀 지저분하게 푼 듯함.. 다시 풀어보겠음

import math

def solution(progresses, speeds):
    answer = []
    
    cur_end_cnt = 0
    cur_day = 0
    
    for i in range(len(progresses)) :
        need_day = math.ceil((100-progresses[i])/speeds[i])
        
        #작업 끝나려면 시간 더 필요
        if cur_day < need_day :
            answer.append(cur_end_cnt)
            #시간 더 흐르도록 함
            cur_day = need_day
            cur_end_cnt = 1
        #이 작업도 끝났음
        else : 
            cur_end_cnt += 1
    answer.append(cur_end_cnt)
    
    return answer[1:]