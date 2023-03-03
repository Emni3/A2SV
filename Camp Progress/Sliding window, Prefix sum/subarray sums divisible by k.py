class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        numd = defaultdict(int)
        numd[0] += 1
        prev = 0
        for i in nums:
            prev += i
            ans += numd[prev % k]
            numd[prev % k] += 1
        return ans
