# pause : 코드는 돌아감. submit 채점 시 fail

'''
길이가 짝수인 실수 배열 nums와 숫자 k가 주어짐. 배열 내의 숫자는 k보다 크지 않음
할 수 있는 연산
- 배열 내의 어떤 숫자든 0~k 중 한 숫자로 바꿀 수 있음
아래 조건을 만족할 때까지 위 연산을 최소 몇번 해야하는가?
-  배열 정 가운데를 기준으로 같은 거리에 있는 두 숫자들의 차의 절댓값이 모두 같음

[1,0,1,2,4,3] 4
1,3 2
0,4 4
1,2 1
-> 누굴 바꾸든 두번 바꿔서 세개를 똑같은 걸로 만들어야 함

[0,1,2,3,3,6,5,4] 6
0,4 4
1,5 4
2,6 4
3,3 0 -> 바꿔야 함 -> 두개를 다 바꿔야 4로 만듦 -> 2번

=> 가장 많이 겹치는 값으로 통일시킨다. -> 여러개면 차가 가장 적은 값으로 통일시킨다
'''
from collections import defaultdict

class Solution(object):
    def minChanges(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        minus_cnt = [0]*(k+1) #이부분 크기가 잘못된듯? n말고 (k+1)로 하니 넘어감
        for i in range(n//2) : 
            minus_cnt[abs(nums[i] - nums[n-i-1])] += 1 #차 개수 셈 #인덱싱에러
        
        minus_often = max(minus_cnt) #가장 많이 등장하는 차 개수
        often_list = []
        for i in range(len(minus_cnt)) :
            if minus_cnt[i] == minus_often : #가장 많이 등장하는 차라면
                often_list.append(i) #모아둠

        # often_list.sort() # 차의 값이 작은 순으로 정렬
        # for minus in often_list : #작은 차부터 돈다

        minus = min(often_list) #가장 작은 차 사용
        print(minus)

        ans = 0
        for i in range(n//2) : 
            if abs(nums[i] - nums[n-i-1]) == minus :
                continue
            
            if k < nums[i]+minus and nums[i]-minus < 0 and k < nums[n-i-1]+minus and nums[n-i-1]-minus < 0 :
                ans += 2
                print("change 2 of %d, %d"%(nums[i], nums[n-i-1]))
            else :
                ans += 1
                print("change 1 of %d, %d"%(nums[i], nums[n-i-1]))

        return ans

# print("ans : %d"%Solution.minChanges([1,0,1,2,4,3], 4)) #통과

print("ans : %d"%Solution.minChanges([1,1,1,1,0,0,0,5,4,3,19,17,16,15,15,15,19,19,19,19], 20)) #output 8, answer 7
