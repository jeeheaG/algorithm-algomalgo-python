# v2 : 정렬, 이진탐색
#시간초과땜에 이진탐색logn 사용
#완전 + 이진 -> nlogn

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
- 2중 완전탐색 : n^2 시간초과
- 완전 + 이진탐색 : nlogn, 통과!
- 탐색 방법
    - 정렬해두고 탐색
    - 젤 작은거 + 더 큰거 로 시작
    - 작은걸 고정해두고 큰걸 옮기면서 반복, 합이 x보다 같거나 작아지면 break
    - 다음 작은 수 탐색
    - 작은 수는 배열 끝까지 탐색
    - 숫자쌍 인덱스 i < j 조건이 있으므로 자기자신 끼리는 안됨

    - (x)수들 중 x보다 큰 수는 처음부터 빼고 탐색 -> 이런 입력이 있는지 잘 모르겠음. 이 부분 추가하니까 성공하던 것도 시간초과나서 제외
'''

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

cnt = 0
#완전탐색
for i in range(N) :
    #이진탐색
    start, end = i+1, N-1
    while start <= end :
        mid = (start + end) // 2
        
        res =  nums[i] + nums[mid]
        if res < x :
            start = mid + 1
        elif res == x :
            cnt += 1
            break
        elif x < res : 
            end = mid - 1

print(cnt)