'''
하루에 과제 하나. 마감일. 점수 많게

점수 최대값은?

7
4 60
4 40
1 20
2 50
3 30
4 10
6 5


4 60
2 50
4 40
3 30
1 20
4 10
6 5

6 5
4 60
4 40
4 10
3 30
2 50
1 20

-> 힙 쓰는 솔루션 기억안나서 봤다. 딱히 힙을 써야 한다기 보다는 그냥 점수순 최대로 정렬해 두면 됨..

점수 큰 순으로 정렬해두고
마감일에 가장 가까운 날짜에 배치하는 방식

'''

import sys
input = sys.stdin.readline

N = int(input())
works = []
last_day = 0
for _ in range(N) :
    day, score = map(int, input().split())
    last_day = max(last_day, day)
    works.append((score, day))

works.sort(reverse=True)
calendar = [True]*(last_day+1) # 비어있으면 True

ans = 0
for score, day in works :
    for i in range(day, 0, -1) :
        if calendar[i] :
            calendar[i] = False # 해당 날짜에 과제 배정
            ans += score
            break
print(ans)