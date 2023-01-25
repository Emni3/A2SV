class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small = 0
        large = len(numbers)-1
        currSum = 0
        while numbers[small] + numbers[large] != target:
            currSum = numbers[small] + numbers[large]
            if currSum > target:
               large -= 1
            else:
                small += 1
        return [small + 1, large + 1]
