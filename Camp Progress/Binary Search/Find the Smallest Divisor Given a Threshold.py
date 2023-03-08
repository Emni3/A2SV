class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divide(arr, m):
            s = 0
            for i in arr:
                s += ceil(i / m)
            return s 

        l = 1
        r = max(nums)
        ans = max(nums)
        while l <= r:
            mid = (l + r) // 2
            if divide(nums, mid) > threshold:
                l = mid + 1
            elif divide(nums, mid) <= threshold:
                ans = mid
                r = mid - 1
        return ans
            
