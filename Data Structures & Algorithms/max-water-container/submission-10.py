class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestArea = 0
        i = 0
        j = len(heights) - 1
        while(i < j):
            len1 = heights[i]
            len2 = heights[j]
            width = j-i
            if(min(len1,len2) * width > bestArea):
                #print(len1,len2,width, min(len1,len2) * width)
                bestArea = min(len1,len2) * width
            if(len1 < len2):
                i+=1
            elif(len2 < len1):
                j-=1
            else:
                i+=1
                j-=1
        return bestArea
