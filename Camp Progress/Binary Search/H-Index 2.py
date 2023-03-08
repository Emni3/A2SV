class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations)-1
        n = len(citations)
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] == (n - mid):
                return citations[mid]
            elif citations[mid] > (n - mid):
                r = mid - 1
            elif citations[mid] < (n - mid):
                l = mid + 1
        #print(l, r, n)
        return n - l
