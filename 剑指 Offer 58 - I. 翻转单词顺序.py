class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split()
        res = ""
        for i in range(len(s_split) - 1, -1, -1):
            res += s_split[i] + ' '
        return res[:-1]