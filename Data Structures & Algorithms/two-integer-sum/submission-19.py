class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            temp = target - value
            if temp in seen:
                return [seen[temp], index]
            else:
                seen[value] = index
            