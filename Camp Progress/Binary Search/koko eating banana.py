class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            hrs = 0
            for i in piles:
                hrs += ceil(i / mid)
            if hrs <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l
