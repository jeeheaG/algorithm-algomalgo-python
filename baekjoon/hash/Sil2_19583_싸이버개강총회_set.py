# v2 : 해시 - set
#알고리즘은 별거없는데 입력이나 시간 데이터 전처리가 귀찮았
# TS 1 : sys.stdin.readlines() 는 입력의 끝부분까지 전부 입력받아온다. 입력의 개수를 알 수 없을 때 사용!
#           Ctrl+Z+엔터가 터미널 입력시 파일의 끝을 의미하므로 입력 끝까지 받는 테스트 시 사용할 것!
# TS 2 : 테케 2 오답 -> 이름 두번 세어지는 경우 생각 못함!!! set사용해서 중복없이 세도록 수정
# TIP : dictionary와 set은 공간, 시간복잡도가 거의 차이 안난다. set은 dictionary에서 key만 있는 거라고 보면 됨

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
    time_table.append(str_to_min(time_str))

#채팅기록 입력받기 - 입력의 끝까지 한번에 받음(입력이 총 몇갠지 몰라서)
chats = sys.stdin.readlines() # TS 1

#채팅으로 입퇴장 확인
entered = set() # TIP
success = set() # TS 2
for chat in chats :
    time_str, name = chat.split()
    time = str_to_min(time_str)

    if time <= time_table[0] : #제때 입장한 사람 기록
        entered.add(name)

    elif time_table[1] <= time <= time_table[2] : #제때 퇴장한 사람이고
        if name in entered : #제때 입장한 사람이면
            success.add(name) # TS 2

print(len(success))
