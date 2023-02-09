def flip(arr, index):
    k = 0
    j = index
    while k < index/2 and j > index/2:
        arr[k], arr[j] = arr[j], arr[k]
        k += 1
        j -= 1
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        end = len(arr)-1
        for i in range(end,-1,-1):
            maxi = max(arr[0:i+1])
            index = arr.index(maxi)
            flips.append(index+1)
            flip(arr,index)
            flips.append(i+1)
            flip(arr,i)
            
        return flips
