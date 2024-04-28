#  공익광고가 삽입될 최적의 위치
# 진짜 주먹구구 구현함.. 근데 오답이고 시간초과

def str_to_sec(time_str) :
    return int(time_str[0:2])*60*60 + int(time_str[3:5])*60 + int(time_str[6:8])

def solution(play_time, adv_time, logs):
    answer = ''
    
    #입력을 모두 초단위로 변경
    full_sec = str_to_sec(play_time)
    adv_sec = str_to_sec(adv_time)
    
    logs_sec = []
    for log_str in logs :
        start_sec = str_to_sec(log_str[:8])
        end_sec = str_to_sec(log_str[9:])
        logs_sec.append((start_sec, end_sec))

    # 최대로 재생될 '구간'을 어떻게 할지
    playing_cnt = [0]*full_sec
    for i in range(full_sec) :
        for log in logs_sec :
            if log[0] == i :
                playing_cnt[i] += 1
            if log[1]+1 == i :
                playing_cnt[i] -= 1
            
    # 시작 시각 별 광고재생 총시간 계산
    max_sum = 0
    start_sec = 0
    for i in range(full_sec-adv_sec+1) :
        end = i + adv_sec + 1
        cur_sum = sum(playing_cnt[i:end])
        if max_sum < cur_sum :
            print(max_sum)
            max_sum = cur_sum
            start_sec = i

    hh = start_sec//(60*60)
    mm = (start_sec-hh*(60*60))//60
    ss = (start_sec-hh)%60
    answer = str(hh) + ":" + str(mm) + ":" + str(ss)
    return answer


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))