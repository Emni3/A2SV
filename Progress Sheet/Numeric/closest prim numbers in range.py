class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for i in range(right+1)]
        p = 2
        while (p * p <= right):
            if (prime[p] == True):
                for i in range(p * p, right+1, p):
                    prime[i] = False
            p += 1

        arr = []
        for p in range(2, right+1):
            if prime[p] and p >= left:
                arr.append(p)

        mini = float('inf')
        ans = [-1, -1]
        for i in range(len(arr)-1):
            difference = abs(arr[i] - arr[i+1])
            if difference < mini:
                mini = difference
                ans = [arr[i], arr[i+1]]
                
        return ans
