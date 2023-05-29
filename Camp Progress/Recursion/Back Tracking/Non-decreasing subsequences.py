class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(indx, arr):
            nonlocal ans
            if len(arr) > 1:
                ans.append(arr[:])
            visited = set()
            for i in range(indx, len(nums)):
                if nums[i] not in visited and (not arr or nums[i] >= arr[-1]):
                    visited.add(nums[i])
                    dfs(i + 1, arr + [nums[i]])
        dfs(0, [])
        return ans
