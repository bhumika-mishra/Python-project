file = open('Codingal.txt', 'r')
print(file.read())

file = open('Codingal.txt', 'w')
file.write("Hi there! I hope you’re having a good day.")


file = open('Codingal.txt', 'a')
file.write(" Hi there! I hope you're having a good day.")

file.close()