class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invertReverse(s):
            reversedStr = []
            for i in s:
                if i == "0":
                    reversedStr.append("1")
                else:
                    reversedStr.append("0")
            return "".join(reversedStr)[::-1]
        def solve(i, res):
            if i == n:
                return res[k - 1]
            temp = res + "1" + invertReverse(res)
            return solve(i + 1, temp)
        return solve(1, "0")
