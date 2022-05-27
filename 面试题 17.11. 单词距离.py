class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        """
            先统计单词的下标，两重循环
        """
        word1_index = []
        word2_index = []
        for i in range(len(words)):
            if word1 == words[i]:
                word1_index.append(i)
            if word2 == words[i]:
                word2_index.append(i)
        
        res = 1000000
        for i in word1_index:
            for j in word2_index:
                res = min(res, abs(i - j))
        
        return res