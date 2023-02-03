class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastoccurance = {}
        for i in range(len(s)):
            lastoccurance[s[i]] = i
        res = []
        length, end = 0, 0

        for i in range(len(s)):
            length += 1
            if lastoccurance[s[i]] > end:
                end = lastoccurance[s[i]]
            if i == end:
                res.append(length)
                length = 0   
        return res
