from typing import List
import collections

            
if __name__ == "__main__":
    l1 = [1,1,1]
    l2 = [1,2,3]
    k1 = 2
    k2 = 3

    solution = Solution()
    res1 = solution.subarraySum(l1, k1)
    res2 = solution.subarraySum(l2, k2)
    print(res1)
    print(res2)