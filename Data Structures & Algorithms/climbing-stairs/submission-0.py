class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        
        def fib(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = fib(x - 1) + fib(x - 2) 
            return memo[x]
        return fib(n) 
