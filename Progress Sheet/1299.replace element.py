class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = 0
        maxi = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = maxi
            maxi = max(temp, maxi)
        return arr
