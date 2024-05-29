# v2 : 해시 - set

import sys
input = sys.stdin.readline

N = int(input())

people = set()
for _ in range(N) :
    name, log = input().split()
    if log == "leave" :
        people.discard(name) #discard : 해당 키값 존재여부 상관없이 삭제
    else : #log == "enter"
        people.add(name)


#키값만 사전순 역순으로 출력
#출력 - 그냥 for문 돌면서 이렇게 해도 되고
# for name in sorted(people, reverse=True) :
#     print(name)

#출력 - join써서 이렇게 해도 됨. 이게 훨 빠름!
print("\n".join(sorted(people, reverse=True)))