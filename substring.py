n = input("Enter a string: ")
def substring(s):
    n = len(s)
    total_combinations = 1 << n 
    for i in range(total_combinations):
        substring = ""
        for j in range(n):
            if (i & (1 << j)):
                substring += s[j]
                print(substring)
substring(n)
