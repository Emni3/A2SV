class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        i = 0
        while i < n:
            p = nums[i] - 1
            if nums[p] != nums[i]:
                nums[p], nums[i] = nums[i], nums[p]
            else:
                if i != p:
                    ans.append(nums[i])
                    #print(i, p, ans)
                i += 1
        return set(ans)
