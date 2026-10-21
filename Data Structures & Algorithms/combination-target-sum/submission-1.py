class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, path):
            if sum(path) == target:
                result.append(path[:])
                return
            if(sum(path) > target):
                return
            if index == len(nums):
                return
            path.append(nums[index])
            backtrack(index,path)
            path.pop()

            backtrack(index+1,path)
        
        backtrack(0,[])
        return result
