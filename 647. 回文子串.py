class Solution:
    def countSubstrings(self, s: str) -> int:
        """
            以每个单词为中心词，分别计算长度为偶数和奇数时的回文串数目
        """
        res = 0
        for i in range(len(s)):
            l, r = i ,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res