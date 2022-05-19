from typing import List
import collections

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        if n == 1:
            return [-1]
        
        for i in range(n):
            intervals[i].append(i)
        intervals.sort()

        res = [-1] * n
        for i in range(n):
            l, r = 0, n - 1
            while l < r:
                mid = (l + r) // 2
                if intervals[mid][0] < intervals[i][1]:
                    l = mid + 1
                else:
                    r = mid
            if intervals[r][0] >= intervals[i][1]:
                res[intervals[i][2]] = res[intervals[r][2]]
        return res
            
if __name__ == "__main__":
    l1 = [[3,4],[2,3],[1,2]]
    l2 = [1,2,3]
    k1 = 2
    k2 = 3
    s1 = "abc"
    s2 = "aaa"
    solution = Solution()
    res1 = solution.findRightInterval(l1)
    # res2 = solution.subarraySum(l2, k2)
    print(res1)
    # print(res2)