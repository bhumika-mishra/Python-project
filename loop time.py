import random 
n = random.randint
n = int(input("Enter a no. : "))
def time_complexity(n):
    print("Analyzing time complexity for n =", n)
    
    first_loop = 0
    for i in range(0, n + 1):
        first_loop += 1
    print(f"First loop ran {first_loop} times")


    second_loop = 0
    j = 1
    while j <= n + 1:
        second_loop += 1
        j =j*2
    print(f"Second loop ran {second_loop} times")


    third_loop = 0
    for i in range(0, 100):
        third_loop += 1
    print(f"Third loop ran {third_loop} times")

time_complexity(n)