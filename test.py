from quicksort import sorting
import time
import random

start_time = time.perf_counter()
sort = sorting()
arr = random.sample(range(1,100),10)
print("array before sorting :" , arr)
end = len(arr)
sort.quick_sort(arr,0,end-1)
print("array after quick sort :",arr)
print("\n")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")


# already sorted array
start_time = time.perf_counter()
sort2 = sorting()
print("array before sorting :" , arr)
end = len(arr)
sort2.quick_sort(arr,0,end-1)
print("array after quick sort :",arr , "\n")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time already sorted array : {elapsed_time:.6f} seconds")


# a reverse sorted array
start_time = time.perf_counter()
sort = sorting()
arr = [10,9,8,7,6,5,4,3,2,1]
print("array before sorting :" , arr)
end = len(arr)
sort.quick_sort(arr,0,end-1)
print("array after quick sort :",arr)
print("\n")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time a reverse sorted array : {elapsed_time:.6f} seconds")


#an array with duplicates elements
start_time = time.perf_counter()
sort = sorting()
arr = [99,5,5,99,8,4,6,3,2,7,4]
print("array before sorting :" , arr)
end = len(arr)
sort.quick_sort(arr,0,end-1)
print("array after quick sort :",arr)
print("\n")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time an array with duplicates elements : {elapsed_time:.6f} seconds")


#an array with single element
start_time = time.perf_counter()
sort = sorting()
arr = [10]
print("array before sorting :" , arr)
end = len(arr)
sort.quick_sort(arr,0,end-1)
print("array after quick sort :",arr)
print("\n")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time an array with single element : {elapsed_time:.6f} seconds")


#an empty array
start_time = time.perf_counter()
sort = sorting()
arr = []
print("array before sorting :" , arr)
end = len(arr)
sort.quick_sort(arr,0,end-1)
print("array after quick sort :",arr)
print("\n")
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time an empty array : {elapsed_time:.6f} seconds")