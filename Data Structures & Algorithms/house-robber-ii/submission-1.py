class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        def houses(nums, maxP):
            best = {
                0:nums[0],
                1:max(nums[0], nums[1])
                }
            for i in range(2, len(nums) - 1):
                best[i] = max(nums[i] + best[i - 2], best[i - 1])
                maxP = max(maxP, best[i])
            return maxP
        
        def last(nums, maxP):
            best = {
                0:0,
                1:nums[1]
                }
            for i in range(2, len(nums)):
                best[i] = max(nums[i] + best[i - 2], best[i - 1])
                maxP = max(maxP, best[i])
            return maxP
        total = max(houses(nums, 0), last(nums, 0))
        return total

        

