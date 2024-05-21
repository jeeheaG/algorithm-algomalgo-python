from itertools import permutations

N = int(input())

arr = list(permutations(range(1,N+1), N))
arr.sort()

for p in arr :
    str = ''
    for num in p :
        str += f"{num} "
    print(str)