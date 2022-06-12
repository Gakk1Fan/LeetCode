class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
            统计i左边1的个数和右边0的个数
        """
        tot_one = 0
        n = len(s)
        for i in range(n):
            tot_one += s[i] == '1'
        # print(tot_one)
        one = 0
        ans = inf
        for i in range(n):
            if s[i] == '1':
                r0 = (n - i - 1) - (tot_one - 1 - one)
            else:
                r0 = (n - i - 1) - (tot_one - one)
            # print("l1:", one)
            # print("r0:", r0)
            ans = min(ans, r0 + one)
            one += s[i] == '1'
        return ans