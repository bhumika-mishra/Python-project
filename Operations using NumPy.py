import numpy as np 
arr = np.array([0,1,2,3,4,5,6,7,8,9])
k = np.where(arr == 8)
arr1 = np.array([10,11,12,13,14,15,16,17,18,19])
arr2 = np.concatenate((arr,arr1))
arr3 = np.array([3,2,0,1,5,4,6,9])
for x in arr:
    print(x)
print(arr)
print(arr[7]) #indexing
print(arr[1:5]) #slicing
print(arr.dtype) #checking datatype
print(arr2) 
print(k)
print(np.sort(arr3)) #sorting
