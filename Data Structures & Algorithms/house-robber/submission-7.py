class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {
            0:nums[0],
            1:max(nums[0], nums[1])
        }
        best_total = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            memo[i] = max(nums[i] + memo[i-2], memo[i-1])
            best_total = max(best_total, memo[i])
        return best_total



                


