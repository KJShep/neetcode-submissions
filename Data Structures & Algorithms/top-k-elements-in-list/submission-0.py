class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        
        #now make buckets and frequency becomes bucket index
        buckets = [[] for _ in range(len(nums)+1)]
        for key,freq in d.items():
            buckets[freq].append(key)
        
        ans = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                if(k == 0):
                    return ans
                ans.append(num)
                k-=1
        
        return ans