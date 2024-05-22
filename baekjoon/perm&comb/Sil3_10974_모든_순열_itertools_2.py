# v2 : 순열 - itertools 라이브러리 연습
#       join을 사용해서 좀더 간결하게

from itertools import permutations

N = int(input())

arr = list(permutations(range(1,N+1), N))

for p in arr :
    print(' '.join(map(str, p)))