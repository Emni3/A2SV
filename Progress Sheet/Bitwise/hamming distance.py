class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ham = x ^ y
        return ham.bit_count()
