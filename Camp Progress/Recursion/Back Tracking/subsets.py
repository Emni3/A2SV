class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(idx, arr):
            flag = (arr in ans)
            if flag:
                return 
            if not flag:
                ans.append(arr[:])
            
            for i in range(idx, len(nums)):
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()
        backtrack(0, [])
        return ans
