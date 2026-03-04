file = open('Codingal.txt', 'r')
print(file.read())

print(file.readline())
print(file.readline())
print(file.readline())

print(file.readlines())

for x in file:
    print(x)

file.close()
