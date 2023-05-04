class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i]*-1       
        heapify(stones)
        while len(stones) > 1:
            y = heappop(stones) * -1
            x = heappop(stones) * -1 
            if y != x:
                y -= x
                heappush(stones, y * -1)
        if len(stones) == 1:
            return stones[0] * -1
        return 0
