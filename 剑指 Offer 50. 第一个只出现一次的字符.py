class Solution:
    def firstUniqChar(self, s: str) -> str:
        if len(s) == 0:
            return ' '
        d = collections.defaultdict(int)
        for subch in s:
            d[subch] += 1
        
        for k, v in d.items():
            if v == 1:
                return k
        return ' '