class Solution:
    def climbStairs(self, n: int) -> int:
        d = [0] * (n+1)
        d[n] = 1
        d[n-1] = 1
        for i in range(n-2,-1,-1):
            d[i] = d[i+2] + d[i+1]
        return d[0]