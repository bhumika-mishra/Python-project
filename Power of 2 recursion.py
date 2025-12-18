n = int(input("Enter your number : "))
def checkpower(n):
    if (n<=0):
        return False
    if(n==1):
        return True
    if(n%2 == 0):
        return checkpower(n/2)
    return False
if(checkpower(n)):
    print("The no. entered is a power of 2")
else:
    print("The no. entered is not a power of 2")    