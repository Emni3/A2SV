class Solution:
    def minSteps(self, n: int) -> int:
        primFact = []
        p = 2

        while p * p <= n:
            while n % p == 0:
                primFact.append(p)
                n //= p
            p += 1
        if n > 1:
            primFact.append(n)

        return sum(primFact)
