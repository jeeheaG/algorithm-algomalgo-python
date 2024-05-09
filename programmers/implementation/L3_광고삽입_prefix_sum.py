# v1 : 구현 - 누적합
# 누적합 사용해서 구현 도전!
# TS1 : test case 9, 31 fail : 광고시작 시간이 0초인 경우라고 함..
#       -> 파이썬은 리스트 인덱싱 시 의도치않은 음수값이 들어가도 뒤에서부터 인덱싱 시켜주므로 out of bound 오류가 안나고 실행이 됨. 주의!

def str_to_sec(time_str) :
    return int(time_str[0:2])*60*60 + int(time_str[3:5])*60 + int(time_str[6:8])

def sec_to_str(time_sec) :
    ss = time_sec%60
    mm = (time_sec//60)%60
    hh = time_sec//(60*60)
    return f'{hh:02}:{mm:02}:{ss:02}'

def solution(play_time, adv_time, logs):
    
    #입력을 모두 초단위로 변경
    full_sec = str_to_sec(play_time)
    adv_sec = str_to_sec(adv_time)
    
    #누적합 구하는 부분 다시짜기
    #+- 배열
    view = [0]*(full_sec+1)
    for log_str in logs :
        start_sec, end_sec = map(str_to_sec, log_str.split('-'))
        view[start_sec] += 1
        view[end_sec] -= 1

    #현재 시청자 수 계산
    for i in range(1, len(view)) :
        view[i] = view[i-1] + view[i]
    
    #누적합 배열 계산
    for i in range(1, len(view)) :
        view[i] = view[i-1] + view[i]

    
    #모든 시간대 탐색
    max_sum_idx = 0
    max_sum = 0
    for j in range(full_sec+1) :
        adv_end_sec = j + adv_sec
        
        #광고가 끝까지 담길 수 없는 시간대까지 갔다면 탐색 중지
        if full_sec < adv_end_sec :
            break
    
        #현재 시각부터 광고 시작 시 시청합계 최대값 구함
        if j != 0 :
            cur_sum = view[adv_end_sec-1] - view[j-1] 
        else : 
            cur_sum = view[adv_end_sec-1] # TS1 : j == 0 이어서 뺄 값이 없는 부분을 처리해줘야 함!!

        if max_sum < cur_sum :
            max_sum_idx = j
            max_sum = cur_sum
    
    return sec_to_str(max_sum_idx)

# 테스트
# print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))

print(solution("02:03:55", "00:14:15", ["00:00:00-00:13:14"])) # TS1 : 9, 31 fail 반례 : 0부터 시작하는 것이 답인 경우