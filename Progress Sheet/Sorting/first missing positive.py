class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxi = len(nums)
        arr = [0 for _ in range(maxi + 1)]
        
        for i in range(len(nums)):
            if nums[i] <= maxi + 1 and nums[i] >= 0:
                arr[nums[i]-1] += nums[i]
        
        for i in range(len(arr)):
            if arr[i] == 0:
                return i + 1
        return 1
