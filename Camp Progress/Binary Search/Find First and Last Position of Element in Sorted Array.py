class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]

        ans = [-1, -1]
        ans[0] = bisect_left(nums, target)
        ans[1] = bisect_right(nums, target) - 1

        return ans
