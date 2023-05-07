class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]

        heapify(piles)
        for i in range(k):
            stone = -heappop(piles)
            stone = ceil(stone/2)
            heappush(piles, -stone)

        total = abs(sum(piles))
        return total
