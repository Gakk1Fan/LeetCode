class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]
            t = int(s[i-2]) * 10 + int(s[i-1])
            if 10 <= t <= 25:
                dp[i] += dp[i-2]
        return dp[n]