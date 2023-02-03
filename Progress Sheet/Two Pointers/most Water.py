class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        maxArea = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                maxArea = max(maxArea, area)
                left += 1
            else:
                area = height[right] * (right - left)
                maxArea = max(maxArea, area)
                right -= 1
        return maxArea
      
