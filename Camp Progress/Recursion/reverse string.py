class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def revers(i, j):
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            if i >= j:
                return
            else:
                revers(i, j)
            
        revers(0, len(s)-1)
