class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(max(count.values()) + 1)]

        for key, value in count.items():
            freq[value].append(key)
        
        ans = []
        while k > 0:
            app = freq.pop()
            ans += app
            k -= len(app)

        return ans
