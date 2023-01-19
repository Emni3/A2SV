class Solution: 
    def select(self, arr, i):
        # code here 
        return 
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
                    
        return arr
