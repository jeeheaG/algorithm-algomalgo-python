'''
문자열s가 주어지고 아래 연산을 할 수 있음
- 양쪽방향에 동일한 문자가 있는 한 문자를 선택해
    양쪽방향에서 가장 가까운 동일문자를 하나씩 지운다
이 연산을 횟수제한 없이 실행 후 얻을 수 있는 문자열 최소길이는?

abaacbcbb
3개 이상 존재하는 문자 중 고를 수 있음
a 3개 - 1번 가능. 1개남음
b 4개 - 1번 가능. 2개남음
c 2개 - 0번 가능. 2개 남음

abcde
1 0 1

aaabaaac
a 6개 - 2번 가능. 2개 남음 abac


ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj

문자열마다 개수 세서 최종 남는 거 계산
    (x) 남는 개수 = 원래개수 - (원래개수//3)*2 -> 위에 긴 예시 fail
원래개수가 홀수개면 1개, 짝수개면 2개 남음

개수세는 건.. 하나씩 pop하면서 defaultdict +1
'''

from collections import defaultdict


class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        cnt_dict = defaultdict(int)

        for ch in s :
            cnt_dict[ch] += 1
        
        ans = 0
        for cnt in cnt_dict.values() :
            ans += 2 if cnt%2 == 0 else 1
        
        return ans