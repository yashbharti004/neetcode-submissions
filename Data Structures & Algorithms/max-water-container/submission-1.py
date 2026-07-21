class Solution:
    def maxArea(self, heights: List[int]) -> int:
        high = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            n = (right - left) * min(heights[left], heights[right])
            high = max(high, n)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return high

        