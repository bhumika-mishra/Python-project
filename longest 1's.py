num = int(input("Enter a number: "))
def consecutiveones(n):
    count = 0
    while n > 0:
        n = n & (n << 1)
        count += 1  
    return count
result = consecutiveones(num)
print(f"Longest consecutive 1's length : {result}")