# v1 : union find (합집합)
# TS : 출력초과??? - 답보다 글자수 자체가 많은 경우에도 오답이 아닌 출력초과가 뜰 수 있다고 함. 틀렸습니다 랑 동일하다는 의미 ex) 답은 1인데 내 출력은 100일 경우 한글자보다 많은 세글자 출력임
#       -> 로직 상 실수가 있었음 해결했음ㅎ
#           union find 짤 때 모든 연산은 루트노드 기준으로 할 것 기억하기..~!
# TIP : 출력은 한번에 - 반복문 안에서 print 바로바로 하는 것보다 함수에서 전달전달 받느라 번거롭더라도 list에 append해뒀다가 한번에 출력하는 게 속도가 빠르다!

'''
[문제 해석]
- sns 친구추가(합집합 연산) 시마다 그 새로운 친구 네트워크에 포함된 전체 친구 수 구하기
- 친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말함
- 친구 = 노드, 친구관계 = 간선
- 시간제한 3초
- 친구관계 수 <= 100000
앗.. 사이클이 생길수도 있겠네..? 같은 네트워크면 친구추가 무시해야겠다
노드가 친구이름으로 주어지니까 딕셔너리를 쓰자

구상 : 노드이름 문자열에 해당하는 번호를 따로 적어두고 사용
- 노드이름에 해당하는 번호를 dict에 적어두고 사용함. 번호가 아직 없는 새 이름이면 번호를 매겨 사용
- union find 에서 부모노드를 적어놓는 배열 list사용
- 각 트리의 원소개수를 적어두는 배열을 사용함. 트리의 루트노드번호를 인덱스로 갖고 원소개수를 값으로 가짐
- x, y 친구 추가 시
    - x의 루트노드!의 자식노드로 y의 루트노드!를 넣음
    - x의 루트노드의 원소 개수에 y의 루트노드의 원소 개수를 더해서 새로운 원소 개수를 업데이트 해줌
나머지 로직은 동일. 거꾸로 번호에서 이름을 찾아야 하는 경우가 없어서 괜찮을 것 같음. 츄라이


구상 2 : 노드이름 문자열 그대로 사용 (이건 구현 안해봤음)
- 노드이름이 문자열이므로, union find 에서 부모노드를 적어놓는 배열로 list대신 dictionary를 사용함
- 친구관계에서 앞 친구의 자식노드로 뒷 친구를 넣음
- 해당 친구 네트워크의 루트노드 이름을 해당 그래프의 이름으로 사용함
- 그래프 이름을 키, 네트워크의 노드 수를 값으로 갖는 딕셔너리에 노드 수를 카운트함
'''

import sys
input = sys.stdin.readline


def union(x, y) :
    root_x, root_y = find(x), find(y)
    
    #이미 같은 친구네트워크라면 그냥 넘어감
    if root_x == root_y :
        return cnt_arr[root_x]

    #다른 트리라면 한쪽 트리의 루트에 추가
    parent[root_y] = root_x # TS : 루트를 옮겨야 그 네트워크 전체가 가서 합집합연산이 성립함..~~!~!
    cnt_arr[root_x] += cnt_arr[root_y] #새로 추가된 친구가 포함된 트리의 원소개수를 새 루트 원소개수에 합쳐줌


    #해당 루트의 트리 원소 개수
    return cnt_arr[root_x]
    

#루트 찾아주는 메서드 +경로압축
def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x]) #경로압축
    return parent[x] #루트가 아니라도 경로압축해서 이미 루트로 업데이트 되어있음


def sol () :
    res = []
    for _ in range(int(input())) :
        friend_add = input().split()

        #친구번호 가져오기
        idxs = [-1,-1]
        for i in range(2) :
            friend = friend_add[i]

            #새로 등장한 이름
            if not friend in friend_nums :
                num = len(friend_nums)
                friend_nums[friend] = num
                parent.append(num) #트리 부모노드 번호표에 추가
                cnt_arr.append(1) #루트노드의 그래프 원소 개수세기표에도 추가
            
            idxs[i] = friend_nums[friend]

        #친구번호로 트리에 넣고 해당 친구네트워크 원소 수 구해 출력
        # print(union(idxs[0], idxs[1]))
        res.append(union(idxs[0], idxs[1]))
    return res

ans = []
for _ in range(int(input())) :
        
    friend_nums = {} #문자열 이름별 숫자 인덱스 적어두는 곳
    cnt_arr = [] #해당 인덱스가 루트노드인 트리(친구네트워크)의 원소개수 적어두는 곳
    parent = [] #트리 부모노드 적어두는 곳

    ans += sol() # TIP : 출력 모아뒀다 한번에 하는 게 빠름
    # sol()

print('\n'.join(map(str, ans)))