# v1 : 해시
#알고리즘은 별거없는데 입력이나 시간 데이터 전처리가 귀찮았
# TS 1 : sys.stdin.readlines() 는 입력의 끝부분까지 전부 입력받아온다. 입력의 개수를 알 수 없을 때 사용!
# TS 2 : 45%에서 틀렸습니다 -> ??

'''
[문제 해석]
- 제때 입장, 퇴장 모두 확인된 사람 수
- 제때 입장 : 채팅시각이 개총 시작시각보다 작거나 같음
- 제때 퇴장 : 채팅시각이 개총 종료시각보다 크거나 같고 개총 스트리밍 종료시각보다 작거나 같음
-> 즉, 개총 시작시각까지 채팅을 친 기록과 종료 후부터 개총 스트리밍 종료시각까지 채팅을 친 기록 이 두가지가 모두 있는 사람 수 세기
- 시간 데이터는 모두 분단위로 바꿔서 사용
'''

import sys
input = sys.stdin.readline

#문자열 시간을 분단위 숫자로 변환해주는 메서드
def str_to_min(time_str) :
    h, m = map(int, time_str.split(":"))
    return h*60 + m


#시각 3개 입력받기
time_table = []
for time_str in input().split() :
    # print(time_str)
    time_table.append(str_to_min(time_str))
# print(time_table)

#채팅기록 입력받기 - 입력의 끝까지 한번에 받음(입력이 총 몇갠지 몰라서)
chats = sys.stdin.readlines() # TS 1

#채팅으로 입퇴장 확인
entered = {}
cnt = 0
for chat in chats :
    # print(chat)
    time_str, name = chat.split()
    time = str_to_min(time_str)

    if time <= time_table[0] : #제때 입장한 사람 기록
        entered[name] = True

    elif time_table[1] <= time <= time_table[2] : #제때 퇴장한 사람이고
        if name in entered.keys() : #제때 입장한 사람이면
            cnt += 1 #개수 셈

print(cnt)
# print(chats)
