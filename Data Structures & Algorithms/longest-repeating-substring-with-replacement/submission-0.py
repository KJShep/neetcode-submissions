class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        longest = 0
        maxFreq = 0

        for right in range(len(s)):
            # Count the new character entering the window
            counts[s[right]] = counts.get(s[right], 0) + 1
            maxFreq = max(maxFreq, counts[s[right]])

            while(right-left + 1 - maxFreq > k):
                counts[s[left]] -= 1
                left += 1
            
            longest = max(longest,right-left+1)
        return longest
