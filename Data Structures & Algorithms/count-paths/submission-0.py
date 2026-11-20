class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [([0] * (n+1)) for _ in range(m+1)]
        d[m-1][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                d[i][j] = d[i+1][j] + d[i][j+1] + d[i][j]
        return d[0][0]
        
        