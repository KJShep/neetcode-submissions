class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]),self.helper(nums[1:]))

    def helper(self, nums):
        n = len(nums)
        d = [-1] * (n+1)
        d[n] = 0
        d[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            d[i] = max(d[i+1],d[i+2] + nums[i])
        return d[0]