class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums) == 0):
            return -1
        startIndex = 0
        if(len(nums) == 1):
            pass
        else:
            l = 0
            u = len(nums)-1
            startIndex = 0
            while(l<=u):
                m = math.floor((u+l)/2)
                if(m==0):
                    if(nums[1] < nums[0]):
                        startIndex = 1
                        break
                    else:
                        startIndex = 0
                        break
                if(nums[m-1] > nums[m]):
                    startIndex = m
                    break
                if(nums[u] > nums[m]):
                    u = m-1
                else:
                    l = m+1
        left = self.binarySearchInc(0,startIndex-1,nums,target)
        right = self.binarySearchInc(startIndex,len(nums)-1,nums,target)

        if left == -1:
            if right == -1:
                return -1
            else:
                return right
        else:
            return left
    
    def binarySearchInc(self, l,u,arr,target):
        while(l<=u):
            m = math.floor((u+l)/2)
            if arr[m] == target:
                return m
            if arr[m] < target:
                l = m+1
            else:
                u = m-1
        return -1

            