# v1 : hash

'''
[문제 해석]
주어진 의상으로 만들 수 있는 서로 다른 코디의 개수는?
코디는 의상 최소 1개를 포함해야함. 같은 종류의 의상 여러개는 못입음
-> 의상 종류별 개수를 세고, 각 종류별 개수+1한 값을 모두 곱한 것에서 -1(아무것도 안입는 경우 제외)한 값

ex)
hat headgear
turban headgear
sunglasses eyewear

headgear 2
eyewear 1

2 1 -> 3*2 - 1 = 5
'''

from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())

ans = []
for _ in range(T) :
    cnt_dict = defaultdict(int)

    for _ in range(int(input())) :
        _, category = input().split()
        cnt_dict[category] += 1

    res = 1
    for val in cnt_dict.values() :
        res *= (val+1)

    ans.append(res-1)

print('\n'.join(map(str, ans)))