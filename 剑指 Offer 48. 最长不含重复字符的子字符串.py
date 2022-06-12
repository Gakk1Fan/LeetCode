class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = collections.defaultdict(int)
        j = 0
        res = 0
        for i in range(len(s)):
            cnt[s[i]] += 1
            while cnt[s[i]] > 1:
                cnt[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res