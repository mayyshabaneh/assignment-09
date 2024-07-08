class sorting:
    def choosePivot(self,arr):
        left = arr[0]
        mid = arr[(len(arr)-1) // 2 ]
        right = arr[len(arr)-1]

    def quick_sort (self,arr,start,end):
        if start < end :
            part_index = self.partiotion(arr,start,end)
            self.quick_sort(arr,start,part_index-1)
            self.quick_sort(arr,part_index+1,end)

    def partiotion(self,arr,start,end):
        pivot = arr[end ]
        i = start-1
        for j in range (start,end):
            if arr[j]<pivot:
                i += 1
                arr[i] , arr[j] = arr[j] , arr[i]
        arr[i+1] , arr[end] = arr[end] , arr[i+1]
        return i+1    
