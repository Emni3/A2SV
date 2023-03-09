class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backTrack(curr_num, arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
              
            for i in range(curr_num+1, n+1):
                arr.append(i)
                backTrack(i, arr)
                arr.pop()

        for i in range(1, n+1):
            backTrack(i, [i])

        return ans
