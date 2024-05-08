# v2 : 큐
# 입출력순서, 차례차례 언급이 있는 문제는 스택/큐 문제로 접근해보기
# TIP : 리스트에 pop()하면 스택, pop(0)하면 큐로 간단히 쓸 수 있다.

def solution(progresses, speeds):
    answer = []
    
    cur_end_cnt = 0
    cur_day = 0
    
    while progresses :
        if 100 <= (progresses[0] + speeds[0]*cur_day) :
            cur_end_cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        else :
            if cur_end_cnt != 0 :
                answer.append(cur_end_cnt)
                cur_end_cnt = 0
            cur_day += 1
        
    answer.append(cur_end_cnt)
    
    return answer