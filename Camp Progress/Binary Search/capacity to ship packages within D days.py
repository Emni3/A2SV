class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(mid):
            ship = 1
            currCap = mid
            for w in weights:
                if currCap - w < 0:
                    ship += 1
                    currCap = mid
                currCap -= w
            return ship <= days        
            
                    
        l = max(weights)
        r = sum(weights)
        least = sum(weights)
        while l <= r:
            mid = (l + r) // 2
            if canShip(mid):
                least = min(mid, least)
                r = mid - 1
            else:
                l = mid + 1
        return least
