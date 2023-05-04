class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.large = nlargest(self.k, nums)
        heapq.heapify(self.large)
        

    def add(self, val: int) -> int:
        heappush(self.large, val)
        while len(self.large) > self.k:
            heappop(self.large)
        return self.large[0]
