# v1 : 해시

import sys
input = sys.stdin.readline

N = int(input())

people = {}
for _ in range(N) :
    name, log = input().split()
    if log == "leave" :
        del people[name]
    else : #log == "enter"
        people[name] = True #암것도 저장 안해도 돼서 암거나 저장


#키값만 사전순 역순으로 출력
#출력 - 그냥 for문 돌면서 이렇게 해도 되고
# for name in sorted(people.keys(), reverse=True) :
#     print(name)

#출력 - join써서 이렇게 해도 됨. 이게 훨 빠름!
print("\n".join(sorted(people.keys(), reverse=True)))