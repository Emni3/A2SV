class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        first = 0
        next = len(nums)-1
        operations = 0
        nums.sort()
        while first < next:
            if nums[first] + nums[next] > k:
                next -= 1
               
            elif nums[first] + nums[next] < k:
                first += 1
            else:
                first += 1
                next -= 1
                operations += 1
        return operations
