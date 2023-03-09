class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        flags = [False] * len(nums)
        def backtrack(arr, flag):
            if all(flag):
                ans.append(arr[:])
                return
                
            for i in range(len(nums)):
                if not flag[i]:
                    flag[i] = True
                    arr.append(nums[i])
                    backtrack(arr, flag)
                    arr.pop()
                    flag[i] = False

        backtrack([], flags)
        return ans
