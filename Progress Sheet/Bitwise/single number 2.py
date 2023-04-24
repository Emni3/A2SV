class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      #with extra space
        count = Counter(nums)
        for k, v in count.items():
            if v == 1:
                return k
