class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+= 1
            j-=1


"""
        def rev(i,j):
            s[i], s[j]= s[j],s[i]
            i += 1
            j -= 1
            if i >= j:
                return
            rev(i,j)
        rev (0,len(s)-1)

"""
