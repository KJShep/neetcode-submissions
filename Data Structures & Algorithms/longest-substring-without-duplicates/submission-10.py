class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        mySet = set()
        length = 0
        i = 0
        left = 0
        while(i < len(s)):
            length = len(mySet)
            mySet.add(s[i])
            if(length == len(mySet)): #duplicate
                if length > longest:
                    longest = length
                #continuously remove
                while(True):
                    mySet.remove(s[left])
                    if(s[left] == s[i]):
                        left+=1
                        break
                    left+=1
                    
                continue
            else:
                i+=1
        print(mySet)
        if len(mySet) > longest:
            longest = len(mySet)
        return longest

