binary = input("Enter a binary number: ")
decimal = 0

for i in range(len(binary)):
    decimal = decimal * 2 + int(binary[i])
print("Decimal value:", decimal)