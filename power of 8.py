n = int(input("Enter your number : "))
def isPowerOfeight(x):
    if ( x == 0):
        return False
    else:
        while(x % 8 == 0):
            x /= 8
        return (x == 1)    
if (isPowerOfeight(n)):
    print("The no. entered is a power of 8")
else:
    print("The no. entered is not a power of 8")    