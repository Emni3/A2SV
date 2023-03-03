class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        prev = 0
        for num in nums:
            self.prefix_sum.append(num + prev)
            prev += num

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            ans = self.prefix_sum[right] - self.prefix_sum[left -1]
        else:
            ans = self.prefix_sum[right] 
        return ans

        
