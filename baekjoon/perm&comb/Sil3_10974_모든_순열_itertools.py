# v1 : 순열 - itertools 라이브러리 연습

from itertools import permutations

N = int(input())

arr = list(permutations(range(1,N+1), N))

for p in arr :
    answer = ''
    for num in p :
        answer += f"{num} " #문자열 포매팅 - 변수 출력
    print(answer)