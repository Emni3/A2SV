class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # running_sum method since the sequence doesn't matter
        
        total = sum(nums)
        prevsum = 0
        for i in range(len(nums)):
            rightsum = total - nums[i] - prevsum
            if rightsum == prevsum:
                return i
            prevsum += nums[i]
        return -1
    
    # o(n) & constant space
                
