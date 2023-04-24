class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factor = set()
        for i in nums:
            d = 2
            while d * d <= i:
                while i % d == 0:
                    i //= d
                    factor.add(d)
                d += 1
            if i >1:
                factor.add(i)
        return len(factor)
