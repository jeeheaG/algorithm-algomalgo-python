'''
주차요금 계산

기본요금, 이후요금

출차시각이 없으면 23:59 출차로 간주


[구상]
일단 시간을 다 분으로 바꿈
하루동안의 누적 분 계산해서 기본+추가요금 계산
추가시간은 올림으로 요금계산

defaultdict(int)에 key=val로 넣음 
차량번호=누적시간

누적시간대로 그냥 요금 계산

"05:34 5961 IN", 
"06:00 0000 IN", 
"06:34 0000 OUT", 
"07:59 5961 OUT", 
"07:59 0148 IN", 
"18:59 0000 IN", 
"19:09 0148 OUT", 
"22:59 5961 IN", 
"23:00 5961 OUT"
'''

from collections import defaultdict

# 시각을 분단위로 변환해주는 메서드
# 01:10 -> 70
def timeToMin(time) :
    hh, mm = map(int, time.split(":"))
    if hh != 0 :
        mm += hh*60
    return mm

def solution(fees, records):
    in_dict = dict()
    accum = defaultdict(int)
    
    # 누적 시간 계산
    for rec in records :
        time, car, status = rec.split()
        
        time = timeToMin(time)
        if status == "IN" :
            in_dict[car] = time
        else :
            in_rec = in_dict[car]
            del in_dict[car]
            
            accum[car] += time - in_rec
    
    # 출차 안된 차량 계산
    if in_dict :
        time = timeToMin("23:59")
        for car, in_rec in in_dict.items() :
            accum[car] += time - in_rec
    
    # 시간에 따른 비용 계산
    
    answer = []
    base_t, base_c, add_t, add_c = fees
    for car, time in accum.items() :
        # 기본시간 이하일 경우
        if time <= base_t :
            answer.append((car, base_c))
            continue
        
        # 기본시간 초과 경우
        add = time - base_t
        add_cnt = add//add_t
        if add % add_t != 0 : #올림해야하면
            add_cnt += 1
        answer.append((car, base_c + add_cnt*add_c))
        
    answer.sort() # 번호 작은 순
    return [cost for _, cost in answer]# 금액만