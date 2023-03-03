class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = []
        prev = 0
        for num in nums:
            prev += num
            run_sum.append(prev)
        return run_sum

