class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
            时间复杂度O(n)
            找到第一个破坏递增性质的l和r
                [0, l]的任何一个数都小于[l+1, n-1]->找到[0,l]中小于等于[l+1, n-1]间最小的数
                [r, n-1]的任何一个数都大于[0, r-1]->找到[r, n-1]中大于等于[0, r-1]间最大的数
        """
        l, r = 0, len(nums) - 1
        while l + 1 < len(nums) and nums[l] <= nums[l + 1]:
            l += 1
        if l == r:
            return 0
        while r - 1 >= 0 and nums[r] >= nums[r - 1]:
            r -= 1
        
        for i in range(l + 1, len(nums)):
            while l >= 0 and nums[l] > nums[i]:
                l -= 1
        
        for i in range(r - 1, -1, -1):
            while r < len(nums) and nums[r] < nums[i]:
                r += 1
        
        return r - l - 1