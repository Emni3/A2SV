class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        d = [-1 for i in range(len(nums))]
        for i in nums:
            d[i-1] = i
        for i in range(len(d)):
            if d[i] == -1:
                ans.append(i+1)
        return ans
