class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowCounter = {}
        wordCounter = {}
        shortestLength = float("inf")
        leftIndex = 0
        rightIndex = 0
        for c in t:
            wordCounter[c] = wordCounter.get(c,0)+1
        shortest = 0
        left = 0
        for right in range(len(s)):
            windowCounter[s[right]] = windowCounter.get(s[right],0)+1
            validWindow = True
            for key in wordCounter:
                if(wordCounter[key] > windowCounter.get(key,0)):
                    validWindow = False
                    break
            if(validWindow):
                validWindow = True
                while(validWindow):
                    windowCounter[s[left]]-=1
                    left += 1
                    for key in wordCounter:
                        if(wordCounter[key] > windowCounter.get(key,0)):
                            validWindow = False
                            break
                left-=1
                windowCounter[s[left]]+=1
                length = right - left + 1
                if(length < shortestLength):
                    shortestLength = length
                    leftIndex = left
                    rightIndex = right
        if(shortestLength == float("inf")):
            return ""
        return s[leftIndex:rightIndex+1]
