class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mountain = True
        peak = arr.index(max(arr))
        inc = 0
        dec = peak
        
        if len(arr) < 3 or arr.count(max(arr)) > 1:
            return not mountain
        if peak == 0 or peak == len(arr)-1:
            return not mountain
        while inc < peak:
            if arr[inc] >= arr[inc+1]:
                return not mountain
            inc += 1
            
        
        while dec < len(arr)-1:
            if arr[dec] <= arr[dec+1]:
                return not mountain
            dec += 1
            
        return mountain
