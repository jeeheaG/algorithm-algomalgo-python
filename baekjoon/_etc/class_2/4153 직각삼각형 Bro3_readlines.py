# BJ CLASS 2
# 파일의 끝까지 입력받는 readlines 사용

import sys
coms = sys.stdin.readlines() #파일의 끝까지 입력받아서 개행문자로 구분해 리스트로 저장

answer = []

for com in coms : #입력 한줄씩 사용
    nums = list(map(int, com.split()))
    nums.sort()
    if nums[0]==0 and nums[1]==0 and nums[2]==0 :
        break

    answer.append("right" if nums[0]**2 + nums[1]**2 == nums[2]**2 else "wrong")

print("\n".join(answer))
