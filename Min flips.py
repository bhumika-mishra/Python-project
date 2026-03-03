def min_flips(arr):
    zeros = 0
    ones = 0

    for num in arr:
        if num == 0:
            zeros += 1
        else:
            ones += 1
    return zeros if zeros < ones else ones

arr = [ 0, 1, 1, 0, 0, 0, 1, 1]
print("Minimum flips needed:", min_flips(arr))
