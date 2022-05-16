class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
            判断相邻两个字符串是否是按照字典序排列
        """
        order_dict = {c: i for i, c in enumerate(order)}
        def cmp(w1, w2):
            for i in range(min(len(w1), len(w2))):
                if order_dict[w1[i]] < order_dict[w2[i]]:
                    return True
                elif order_dict[w1[i]] > order_dict[w2[i]]:
                    return False
            return len(w1) <= len(w2)
        
        for i in range(len(words) - 1):
            if not cmp(words[i], words[i + 1]):
                return False
        return True