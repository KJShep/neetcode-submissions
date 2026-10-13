class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} #Key:Number Value:Frequency
        for i in nums:
            d[i] = d.get(i,0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num,freq in d.items():
            buckets[freq].append(num)
        
        ans = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                ans.append(num)
                k-=1
                if k == 0:
                    return ans

        
        