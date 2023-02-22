class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        ans = []
        length = len(s) - len(p) 
        for i in range(length+1):
            window = Counter(s[i: i+len(p)])
            if window == target:
                ans.append(i)
        return ans
            
