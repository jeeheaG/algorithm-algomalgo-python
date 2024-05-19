# v1 : 이진탐색
# 그냥 클래식한 이진탐색으로　구현하면　될　것　같은데？
# TS 1 : 클래식해보여도 알고리즘을 외워서 쓰려고 하지 말고 문제에 맞게 말랑하게 생각하거라 . . .
# TS 2 : 이진탐색 시 양쪽 인덱스가 같은 경우도 포함해 탐색해야 함!

import sys
input = sys.stdin.readline

N, total = map(int, input().split())
tree_arr = list(map(int, input().split()))

#주어진 높이로 자른 나무 양을 계산하는 메서드
def cut(limit) :
	get = 0
	for tree in tree_arr :
		if limit < tree :
			get += tree - limit
	return get

answer = 0

#이진탐색
left, right = 0, max(tree_arr)
while left <= right : #TS 2
	mid = (right + left) // 2
	get = cut(mid)
	# print(mid, get)

	#적어도 total만큼의 나무를 가져가야 하므로 total <= get 일 경우를 answer에 저장해둬야 함
	if get < total :
		right = mid - 1 #TS 1
	elif get == total :
		answer = mid
		break
	elif total < get :
		answer = mid
		left = mid + 1 #TS 1

print(answer)
