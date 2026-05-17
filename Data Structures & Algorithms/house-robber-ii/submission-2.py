class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        def circular_houses(nums, end):
            total = max(nums[0], nums[1])
            if end == len(nums) - 1:
                best = {
                0: nums[0],
                1: max(nums[0], nums[1])
            }
            else:
                best = {
                0: 0,
                1: nums[1]
                }
            
            for i in range(2, end):
                best[i] = max(nums[i] + best[i - 2], best[i - 1])
                total = max(total, best[i]) 
            return total
        return max(circular_houses(nums, len(nums) - 1), circular_houses(nums, len(nums)))

        

