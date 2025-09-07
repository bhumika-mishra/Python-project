smallest = int(input("Enter the smallest no."))
largest = int(input("Enter the largest no."))

sm = smallest
lg = largest

while(smallest):
    temp = smallest
    smallest = largest % smallest
    largest = temp

    Lcm = (sm* lg)/largest
print("LCM is :",Lcm )