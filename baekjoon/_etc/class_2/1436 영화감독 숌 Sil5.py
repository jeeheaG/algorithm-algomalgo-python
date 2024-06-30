# BJ CLASS 2

'''
[문제 해석]
666이라는 덩어리가 포함되는 숫자를 가장 작은것부터 셀 때, n번째 작은 수를 출력
- 시간제한 : 2초
- 메모리제한 : 128MB
- N <= 10000
-> 규칙을 어떻게 세우나 했는데 브루트포스라고 한다.
'''

N = int(input())

S = "666"
num = 666
cnt = 1
while True :
    if cnt == N : 
        print(num)
        break

    num += 1

    #이번 숫자가 멸망의 수인지 판별
    cur = str(num)
    for i in range(len(cur)-2) :
        if cur[i:i+3] == S :
            cnt += 1
            num = int(cur)
            break