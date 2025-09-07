import random
password = ""
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
punctuation = "@#*&./-"

characters = uppercase + lowercase + digits + punctuation

length = int(input("Enter desired password length: "))

for i in range(length):
    password += random.choice(characters)

print("Generated password:", password)