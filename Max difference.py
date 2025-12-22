def max_difference(a, a_size):
    leftmax = [0] * a_size
    rightmax = [0] * a_size
    leftmax[0] = a[0]
    for i in range(1, a_size):
        leftmax[i] = max(leftmax[i-1], a[i])
    rightmax[a_size-1] = a[a_size-1]
    for i in range(a_size-2, -1, -1):
        rightmax[i] = max(rightmax[i+1], a[i])
    max_diff = 0
    for i in range(a_size):
        if leftmax[i] >= rightmax[i]:
            diff = leftmax[i] - rightmax[i]
        else:
            diff = rightmax[i] - leftmax[i]
        max_diff = max(max_diff, diff)
    return max_diff

c = [4,5,234,2,6,82,234,5234]
diff = len(c)
print("Max Difference:", max_difference(c, diff))
