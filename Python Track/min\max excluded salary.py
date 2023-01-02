class Solution:
    def average(self, salary: List[int]) -> float:

        salary.sort()
        exclud = salary[1:-1]
        average = sum(exclud) / len(exclud)
        return average
