def single_iteration():
    a = int(input("Enter 'a' for a*b : "))
    b = int(input("Enter 'b' for a*b :"))
    result = a * b
    print("1 iteration :", result)

def multiple_iteration():
    a = int(input("Enter 'a' for a*b : "))
    b = int(input("Enter 'b' for a*b : "))
    n = int(input("Enter number of iterations: "))
    
    for i in range(n):
        result = a * b
        print(f"N iteration {i + 1}: {a} × {b} = {result}")

print("Running single iteration function:")
single_iteration()

print("Running multiple iteration function:")
multiple_iteration()