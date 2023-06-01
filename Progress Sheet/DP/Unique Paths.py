class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for i in range(
            m)]
        dp[-1][-1] = 1
        def numOn(i, j):
            if 0 <= i < m and 0 <= j < n:
                return dp[i][j]
            return 0

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[r][c] += numOn(r+1, c) + numOn(r, c+1)
        
        return dp[0][0]
