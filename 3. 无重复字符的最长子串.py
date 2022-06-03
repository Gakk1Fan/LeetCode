class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = collections.defaultdict(int)
        i, j, res = 0, 0, 0
        while i < len(s):
            cnt[s[i]] += 1
            while cnt[s[i]] > 1:
                cnt[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
            i += 1
        return res