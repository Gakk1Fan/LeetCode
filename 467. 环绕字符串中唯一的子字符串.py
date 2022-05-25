class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        """
            时间复杂度O(n)
            dp[i]，记录以字符i结尾的最大字符串的长度
        """
        dp = [0] * 26
        cur = 1
        dp[ord(p[0]) - ord('a')] = 1
        for p1, p2 in pairwise(p):
            if not (ord(p2) - ord(p1) - 1) % 26:
                cur += 1
            else:
                cur = 1
            idx = ord(p2) - ord('a')
            dp[idx] = max(dp[idx], cur)
        return sum(dp)