# fail : 25% 틀렸습니다 나오는데 예제는 통과고 테케도 구하기가 어려워서 어디서 틀린건지 모르겠다,,,

# TIP : 파이썬은 문자열 수식을 그대로 넣으면 계산해주는 eval() 함수를 쓰면 금방 풀린다고 함
#       근데 안쓰고 풀고 싶었음...ㅎ

'''
1~N
+, -, 숫자잇기
결과가 0인 수식 모두만들기

시간제한 : 1초
3 <= N <= 9 
음..구현인가

결과가 0이 되는 모든 수식을 출력




두 자리에 세 경우 모두 넣어보기
1 2 3
123
1+23
1+2+3 (백트래킹?)
1+2-3
1-23
12+3
12-3
1

이걸 어떻게 백트래킹하지??

1 2 3 4 5 6 7
'''

import sys
input = sys.stdin.readline

T = int(input())

all_ans = []
for _ in range(T) :
    N = int(input())
    ans = []
    stack = [] #dfs 용 - (depth, 합할 숫자배열)
    stack.append((1, [1]))

    while stack :
        depth, nums = stack.pop()

        # 끝까지 더한 수식이면 답인지 확인
        if depth == N :
            if sum(nums) == 0 :
                # print(nums)
                # 숫자배열로 출력 형식에 맞춰 문자열 만듦
                nums_str = []
                for num in nums :
                    num_str = str(abs(num))
                    if 10 <= abs(num) :
                        num_str = " ".join(list(num_str))
                    if 0 < num :
                        if nums_str : # 비어있지 않으면 + 붙여서 넣음
                            nums_str.append("+%s"%(num_str))
                        else :
                            nums_str.append("%s"%(num_str))
                    else :
                        nums_str.append("-%s"%num_str)
                
                ans.append("".join(nums_str))
            continue

        n = depth+1
        new_nums1 = nums.copy()
        new_nums1.append(n)
        new_nums2 = nums.copy()
        new_nums2.append(-1*n)
        stack.append((n, new_nums1))
        stack.append((n, new_nums2))
        
        # 마지막 숫자 꺼내서 부호 확인하고 숫자 만듦
        prev = nums[-1]
        if prev < 0 :
            prev = prev*10 - n
        else :
            prev = prev*10 + n
        nums[-1] = prev
        stack.append((n, nums.copy()))
        
    all_ans.append("\n".join(sorted(ans)))

print("\n\n".join(all_ans))
