class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(s):
            n = len(s)
            dp = [0] * (n + 1)
            dp[0] = 1
            dp[1] = 1 if s[0] != '0' else 0
            
            for i in range(2, n + 1):
                curr = int(s[i-1])
                if curr != 0:
                    dp[i] += dp[i-1]
                if int(s[i-2:i]) <= 26 and int(s[i-2:i]) >= 10:
                    dp[i] += dp[i-2]
            return dp[n]
        return dp(s)

            