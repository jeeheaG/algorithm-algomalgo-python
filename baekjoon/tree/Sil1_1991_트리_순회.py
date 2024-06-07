# v1 : 트리 (dfs)

'''
[문제 해석]
- 주어진 트리를 전위, 중위, 후위 순회한 순으로 각각 출력
- 항상 A가 루트노드임
- 시간제한 : 2초

순회 방식
- 전위 순회 : 루트 → 왼쪽 → 오른쪽 자식 순으로 방문
- 중위 순회 : 왼쪽 → 루트 → 오른쪽
- 후위 순회 : 왼쪽 → 오른쪽 → 루트

구상
일단 트리를 입력받고.. 루트가 누군지 알려주니까 거기서부터 찾아가자
세가지 순회 모두 현재 노드 기준으로 우선순위 먼저인 것부터 재귀호출 돌게 하고, 루트노드를 탐색하는 순서에 현재노드를 답에 추가해주면 된다.
'''

import sys
input = sys.stdin.readline

N = int(input()) #노드 개수
tree = dict()
for _ in range(N) :
    root, l, r = input().split()
    tree[root] = (l, r)
    
start = 'A'
result = []

#해당 노드가 존재하는지 반환해주는 메서드
def is_exist(node) : 
    return node != '.'

# 전위 순회
def preorder_dfs(cur) :
    global result
    left, right = tree[cur]
    result.append(cur)
    if is_exist(left) :
        preorder_dfs(left)
    if is_exist(right) :
        preorder_dfs(right)

preorder_dfs(start)
result.append('\n')

# 중위 순회
def inorder_dfs(cur) :
    global result
    left, right = tree[cur]
    if is_exist(left) :
        inorder_dfs(left)
    result.append(cur)
    if is_exist(right) :
        inorder_dfs(right)

inorder_dfs(start)
result.append('\n')

# 후위 순회
def postorder_dfs(cur) :
    global result
    left, right =tree[cur]
    if is_exist(left) :
        postorder_dfs(left)
    if is_exist(right) :
        postorder_dfs(right)
    result.append(cur)

postorder_dfs(start)

#출력
print(''.join(result))