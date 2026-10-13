class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMults = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                leftMults[i] = 1
                continue
            leftMults[i] = leftMults[i-1]*nums[i-1]
        rightMults = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                rightMults[i] = 1
                continue
            rightMults[i] = rightMults[i+1]*nums[i+1]
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = leftMults[i] * rightMults[i]
        return ans

        