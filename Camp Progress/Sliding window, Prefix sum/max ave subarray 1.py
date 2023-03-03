class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = ans = sum(nums[:k])
        right = 0
        left = 0
        
        for right in range(k, len(nums)):
            sums = sums - nums[left] + nums[right]
            left += 1
            ans = max(ans, sums)
        ans = ans/k

        return ans
