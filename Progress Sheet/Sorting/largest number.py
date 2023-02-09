class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        large = ""
        for i in range(len(nums)-1,-1,-1):
            for j in range(i):
                if str(nums[j+1])+str(nums[j]) > str(nums[j])+str(nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        for k in nums:
            large += str(k)
        return str(int(large))
