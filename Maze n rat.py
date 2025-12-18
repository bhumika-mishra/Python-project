def possiblepaths(n, m):
    if (n == 1) or (m == 1):
        return 1
    else:
     return possiblepaths(n - 1, m) + possiblepaths(n, m - 1)
n = int(input("Enter the no. of rows : "))
m = int(input("Enter the no. of columns : "))
w = possiblepaths(n, m)
print(f"Possible Paths: {w}")