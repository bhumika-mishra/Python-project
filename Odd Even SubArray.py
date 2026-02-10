def longest_subarray(arr):
    n = len(arr)
    max_len = 1
    curr_len = 1
    for i in range(1, n):
        if (arr[i] % 2 == 0 and arr[i-1] % 2 == 1) or (arr[i] % 2 == 1 and arr[i-1] % 2 == 0):
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
        else:
            curr_len = 1

    return max_len
arr = [6,4,9,4,7,2,3,4,2,52]
print("Longest Subarray:", longest_subarray(arr))