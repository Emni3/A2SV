class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        small = 0
        large = len(people) - 1
        ans = 0
        while small <= large:
            if people[small] + people[large] <= limit:
                small += 1
            large -= 1
            ans += 1
        return ans
