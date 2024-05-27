# v1 : ?무슨유형
#전에 풀었던 햄버거 만들기 문제에서 썼던 쌓아두고 지우기 방식 사용!
# TS : 문자열 마지막꺼 지워야 할 때는 그냥 리스트로 담아서 pop하는 게 쉽다 . . .

import sys
input = sys.stdin.readline

N = int(input())

ps_arr = [input().strip() for _ in range(N)]

for ps in ps_arr :
    #VPS인지 판단
    bag = []
    for letter in ps : #한글자씩 순회
        bag.append(letter)
        #이번 문자로 괄호가 하나 완성되었다면 완성된 괄호 제거
        if 2 <= len(bag) :
            if bag[-2] == "(" and bag[-1] == ")" :
                bag.pop()
                bag.pop()

    #이번 문자열이 VPS인가 출력
    print("NO" if bag else "YES")