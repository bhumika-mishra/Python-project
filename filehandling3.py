with open("Codingal.txt", "w") as f:
    f.write("Hello World!!!")
f.close()


with open("Codingal.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
file.close()



file = open('Codingal2.txt', 'x')

import os
if os.path.exists("Codingal5.txt"):
    print("File exists!!!")
else:
    print("The file does not exist")


file = open("Codingal2.txt", "w")  

import os
os.remove("Codingal.txt")