class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        small = 0
        large = len(skill) - 1
        groupSum = skill[0] + skill[-1]
        totalSum = 0
        while small < large:
            if groupSum != skill[small] + skill[large]:
                return -1
            totalSum += (skill[small] * skill[large])
            small += 1
            large -= 1
        return totalSum
