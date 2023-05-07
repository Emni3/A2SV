class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for key,val in count.items():
            heappush(heap,(-val,key))
            
        ans = []
        for i in range(k):
            ans.append(heappop(heap)[1])
        return ans
