class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        if len(deck) == 1:
            return False
        if len(count) == 1:
            return True
        arr = list(count.values())
        gcd = math.gcd(arr[0], arr[1])
        for i in range(len(arr)):
            gcd = math.gcd(gcd, arr[i]) 
        if gcd > 1:
            return True
        else:
            return False
        
