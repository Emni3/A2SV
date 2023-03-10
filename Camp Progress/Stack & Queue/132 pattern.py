class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #pair [curr_num, min_before] decreasing
        stack = [] 
        mini = nums[0]
        
        for i in nums:
            while stack and i >= stack[-1][0]:
                stack.pop()
            if stack and i > stack[-1][1] and i < stack[-1][0]:
                return True
            stack.append([i, mini])
            mini = min(mini, i)
        return False
