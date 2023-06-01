class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = [0 for _ in range(n+2)]
        dp[0] = 0
        dp[1] = 1 
        maxi = 0 if n == 0 else 1

        for i in range(1, n+1):
            if 2 <= 2 * i <= n:
                dp[2 * i] = dp[i]
                maxi = max(maxi, dp[2*i])

            if 2 <= 2 * i + 1 <= n:
                dp[2 * i + 1] = dp[i] + dp[i + 1]
                maxi = max(maxi, dp[2*i+1])
            
        
        return maxi
