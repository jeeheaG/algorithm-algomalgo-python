# v1 : 이진탐색
# 그냥 클래식한 이진탐색으로　구현하면　될　것　같은데？

import sys
input = sys.stdin.readline

N, total = map(int, input().split())
tree_arr = list(map(int, input().split()))

tree_arr.sort()

def cut(limit) :
	get = 0
	for tree in tree_arr :
		if limit < tree :
			get += tree - limit
	return get

answer = 0

#이진탐색
left, right = 0, max(tree_arr)
while left < right :
	mid = (right + left) // 2
	get = cut(mid)
	print(mid, get)

	if get < total :
		print("get <= total")
		answer = mid
		left = mid + 1
	elif get == total :
		print("get <= total")
		answer = mid
		break
	elif total < get :
		right = mid - 1

print(answer)
