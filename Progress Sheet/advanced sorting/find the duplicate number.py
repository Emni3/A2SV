class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = []
        n = len(nums)
        i = 0
        while i < n:
            p = nums[i] - 1
            if nums[p] != nums[i]:
                nums[p], nums[i] = nums[i], nums[p]
            else:
                if i != p:
                    return nums[i]
                i += 1
