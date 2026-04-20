class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        prev2 = 0
        prev1 = nums[0]
        for i in range(1, len(nums)):
            skip = prev1
            rob = nums[i] + prev2
            current = max(skip, rob)
            prev2 = prev1
            prev1 = current
        return prev1



