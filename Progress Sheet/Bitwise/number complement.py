class Solution:
    def findComplement(self, num: int) -> int:
        bit = str(bin(num))
        ans = ""
        for i in bit[2:]:
            if i == '0':
                ans += '1'
            else:
                ans += '0'

        return int(ans, 2)
