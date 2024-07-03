# v1 : greedy
#아이디어 생각하는 거 하나 더 배웠다..~

'''
[문제 해석]
두가지 순위 중 적어도 하나는 선발인원 내 최저순위가 아닌 사람 최대인원수

구상 
아 설명부터 어렵다
일단 각 순위 1등을 뽑아놓고 이 1등의 다른 순위를 이기는 사람을 고름?
순위 합 작은순?
몰라..

-> a순위대로 정렬해두고 차례로 보면서 b순위 기준점을 넘는지 판단.a는 갈수록 낮아지기만 하므로 b만 보면 되는 것..!!..!

예1)
1 4 v -> min_second = 4
2 3 v -> min_second = 3
3 2 v -> min_second = 2
4 1 v -> min_second = 1
5 5 x
=> 4명

예2)
1 4 v -> min_second = 4
2 5 x
3 6 x
4 2 v -> min_second = 2
5 7 x
6 1 v -> min_second = 1
7 3 x
=> 3명
'''

import sys
input = sys.stdin.readline

T = int(input())

ans = []
for _ in range(T) :
    N = int(input())
    ranks = [tuple(map(int, input().split())) for _ in range(N)]
    
    ranks.sort() #앞쪽 등수 순으로 정렬

    cnt = 0
    min_second = N+1 #두번째 등수 최소값 저장
    for rank in ranks :
        # 첫번째 등수가 낮아지는 쪽으로 돌면서, 두번째 등수가 현재까지 선발한 사람들의 최저등수보다 높으면 선발 후 최저등수 갱신
        if rank[1] < min_second :
            cnt += 1
            min_second = rank[1]

    ans.append(cnt)

print('\n'.join(map(str, ans)))