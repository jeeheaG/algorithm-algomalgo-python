# BJ CLASS 2

'''
최대한 적은 개수의 3과 5의 합으로 목표 숫자N 만들기

항상 경우를 잘게 나눠서 생각해볼것~~!!~!
1. 5로 나눠지는지 -> 5로만
2. 5로 안나눠지면 5랑 3조합으로 되는지 -> 어케확인함? 다해봄?
    - 5로 나눈 나머지 -> 1 2 3 4
        - 1 -> 5개수-1, 3 2개
        - 2 -> 5개수-2, 3 4개
        - 3 -> 5개수-0, 3 1개
        - 4 -> 5개수-1, 3 3개
        이 때 빼야하는 5개수만큼 뺄 수 없으면 다음 단계로 넘어감
        
3. 3으로 나눠지는지
4. 암것도 안될때 -> 1, 2, 4, 7 이게 전부임! 더 큰 수는 모두 2번에서 처리가능함
'''

import sys
input = sys.stdin.readline

N = int(input())

#아무것도 안될 때
if N in (1,2,4,7) :
    print(-1)
    sys.exit()

mod_five = N%5
devide_five = N//5

#5로 나눈 나머지에 대한 경우
if mod_five == 0 :
    print(devide_five)
elif mod_five == 1 and 5 <= N :
    print(devide_five+1)
elif mod_five == 2 and 10 <= N :
    print(devide_five+2)
elif mod_five == 3 :
    print(devide_five+1)
elif mod_five == 4 and 5 <= N :
    print(devide_five+2)
#3으로 나줘지는 경우
elif N%3 == 0 :
    print(N//3)