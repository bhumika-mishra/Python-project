#Recursion for -ve no.s
def nrec():
    num = int(input("Enter a number : "))
    if num < 0:
        print("Negative number entered!!!\nStopping recursion..!")
        return
    else:
         print("Number: +ve")
         nrec()  
nrec()
