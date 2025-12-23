def sort012(arr,a_size):
    zero = 0
    one =  0
    two = a_size - 1
    while one <= two:
        if arr[one] == 0:
            arr[zero], arr[one] = arr[one] ,  arr[zero]
            zero += 1
            one += 1
        elif arr[one] == 1:
            one += 1
        else:  
            arr[one], arr[two] = arr[two], arr[one]
            two -= 1
    return arr
arr = [0,1,1,0,1,2,1,2,0,0,0,2]
a_size = len(arr)
print("Sorted Array : ",sort012(arr,a_size)) 