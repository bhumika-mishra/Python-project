def length(list):
    if not list:
        return 0
    else:
     return 1 + length(list[1:])
a = [1,2,234,234,745,3,6,653]
print([1,2,234,234,745,3,6,653])
print(f"Length of Array: {length(a)}")
