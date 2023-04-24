class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def GCD(a, b):
            if b == 0:
                return a
            return GCD(b, a%b)

        ans = 0
        for i in range(len(nums)):
            currGcd = 0
            for j in range(i, len(nums)):
                currGcd = GCD(currGcd, nums[j])
                if currGcd == k:
                    ans += 1
                elif currGcd < k:
                    break
        return ans
