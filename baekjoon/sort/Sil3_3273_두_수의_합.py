# v1 : 정렬?
#테케는 통과하는데 채점 시 시간초과 나는 풀이 . . . 이진탐색으로 해볼까

'''
[문제 해석]
- 주어진 수들 중 두 수의 합이 특정 수x가 되는 경우의 개수
- 숫자는 1~1,000,000 자연수, 숫자의 개수는 100,000 개 이하
- 시간제한 : 1초


[예제]
9
5 12 7 10 9 1 2 3 11
13

-> 정렬 1 2 3 5 7 9 10 11 12

구상
- 시간제한이 1초 = 2천만 건 안에 처리 -> n^2이 나오면 안됨
- 완전탐색?
- 줄일 방법
    - 수들 중 x보다 큰 수는 처음부터 빼고 탐색
    - 정렬해두고 탐색
    - 젤 작은거 + 젤 큰거 로 시작
    - 작은걸 고정해두고 큰걸 줄이면서 반복, 합이 x보다 같거나 작아지면 break
    - 다음 작은 수 탐색
    - 작은 수는 배열 끝까지 탐색
    - 숫자쌍 인덱스 i < j 조건이 있으므로 자기자신 끼리는 안됨
'''

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

cnt = 0
for i in range(N) : #최악의 경우 O(n)=n^2가 나오는 이중for문이긴 한데 논리상 그렇게가진 안나올 것 -> 시간초과당^0^
    for j in reversed(range(N)) : #0~N-1 을 역순으로 돎
        if i >= j :
            break

        res = nums[i] + nums[j]
        # 합이 답이면 개수 +1 후 break, 답보다 작아졌으면 그냥 break
        if res == x :
            cnt += 1
            break
        elif res < x :
            break

print(cnt)