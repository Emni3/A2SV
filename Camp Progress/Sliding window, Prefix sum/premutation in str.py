class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        contains = False
        target = Counter(s1)
        window = defaultdict(int)
        left = 0
        right = len(s1)
        if len(s1) > len(s2):
            return contains
        for i in range(len(s1)):
            window[s2[i]] += 1
        
        while right < len(s2):
            if window == target:
                return not contains
        
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]] 
            left += 1
            window[s2[right]] += 1
            right += 1
        if window == target:
            return not contains

        return contains
