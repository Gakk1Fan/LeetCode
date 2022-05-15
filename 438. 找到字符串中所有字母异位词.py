class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
            滑动窗口
            1. 统计所需要的字符数量
            2. 统计size = len(p)滑动窗口里面的字符的数量

            时间复杂度O(n)
        """
        #  统计p中各个字符所需要的个数
        cnt = collections.Counter(p)
        
        # 如果[j, i]满足n个字符的个数，satisfy = n
        i, j, satisfy = 0, 0, 0
        tot = len(cnt)
        res = []
        while i < len(s):
            cnt[s[i]] -= 1
            if cnt[s[i]] == 0: satisfy += 1
            if i - j + 1 > len(p):
                if cnt[s[j]] == 0: satisfy -= 1
                cnt[s[j]] += 1
                j += 1
            if satisfy == tot:
                res.append(j)
            i += 1
        return res 