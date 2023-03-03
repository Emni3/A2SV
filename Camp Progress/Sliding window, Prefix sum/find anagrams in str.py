class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = {}
        exist = []
        for i in p:
            target[i] = 1
        
        window = {}
        left = 0
        index = 0
        right = len(p)-1
        while right < len(s):
            window[left] = 1
            left += 1
            i

        for i in range(len(s)):
            for w in range(len(p)-1):
                window[i] = 1

            if window == target:
                exist.append(i)

        return exist
