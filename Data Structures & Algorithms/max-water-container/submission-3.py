class Solution:
    def maxArea(self, heights: List[int]) -> int:
        base, width = 0, len(heights) - 1
        maxA = 0

        while base < width:
            length = width - base
            wall = min(heights[base], heights[width])
            maxA = max(maxA, (length * wall))

            if heights[base] > heights[width]:
                width -= 1
            else:
                base += 1


        return maxA