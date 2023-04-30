class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n+1))
        count = 0
        def backtrack(start):
            if start == n:
                nonlocal count 
                count += 1
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                if nums[start] % (start + 1) == 0 or (start + 1) % nums[start] == 0:
                    backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return count
