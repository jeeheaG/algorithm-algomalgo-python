# v1 : 분할정복

'''
[문제해석]
2^N 크기의 정사각형 배열을 Z모양으로 나눠 탐색할 때, 특정 칸을 탐색하는 순서 구하기
Z모양 탐색이란 : 2사분면 > 1사분면 > 3사분면 > 4사분면 순

[구상]
4x4. N=2
4x4/4 = 4 가 제일 큰 사각형 크기.

현재 탐색중인 면 크기 = S
이 중에 누구? r,c 값이 S / 2 보다 큰가?작은가?
그 안에서 다시 2^N/2 /2 
    0  1  2  3
0 | 0  1  4  5
1 | 2  3  6  7
2 | 8  9  12 13
3 | 10 11 14 15
S = 4. S/2 = 2
r = 2, c = 1 -> r > 2, c < 2 -> 3사분면 -> +line^2
좌표의 사분면에 따라 값 더해줌


-> 제일 큰 사각형부터 사분할 하면서 누적값 더함, 좌표이동, 다음 단계 작은 사각형 탐색
'''


N, r, c = map(int, input().split())

def recur(S, r, c, add_sum) :
    if S == 1 :
        return add_sum
    
    add = 0
    line = S//2 # 사분할 기준선 값
    square = line**2 # 통으로 더해줄 값단위
    
    if line <= r :
        add += square*2
        r -= line
    if line <= c :
        add += square
        c -= line

    return recur(line, r, c, add_sum+add) # 그다음 작은 사분할 진행

print(recur(2**N, r, c, 0))