class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        u = len(nums)-1
        l = 0
        while(l < u):
            m = (l+u)//2
            if(nums[m] > nums[u]):
                l = m+1
            else:
                u = m
        return nums[l]