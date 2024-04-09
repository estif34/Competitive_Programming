class Solution: 
    def select(self, arr, i):
        pass
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min = arr[i]
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]