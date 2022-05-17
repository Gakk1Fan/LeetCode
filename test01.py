from typing import List
import collections

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l, r = i ,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res
            
if __name__ == "__main__":
    l1 = [1,1,1]
    l2 = [1,2,3]
    k1 = 2
    k2 = 3
    s1 = "abc"
    s2 = "aaa"
    solution = Solution()
    res1 = solution.countSubstrings(s2)
    # res2 = solution.subarraySum(l2, k2)
    print(s2)
    # print(res2)