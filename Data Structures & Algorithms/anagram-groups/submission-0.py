class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for i,s in enumerate(strs):
            key = sorted(s)
            if tuple(key) not in d:
                d[tuple(key)] = []
            d[tuple(key)].append(i) #turns into array
        ans = [[] for _ in d]
        for i,e in enumerate(d.values()): #every elem
            for index in e: #every elem in array
                ans[i].append(strs[index])
        return ans

            