import random

print("Wellcome to the PyPassword Generator!")
numOfLetters = int(input("How many letters would you like in your password?\n"))
numOfSymbols = int(input("How many symbols would you like?\n"))
numOfNumbers = int(input("How many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

for i in range(0, numOfLetters):
    password.append(letters[random.randint(0, len(letters) - 1)])

for i in range(0, numOfSymbols):
    password.append(symbols[random.randint(0, len(symbols) - 1)])

for i in range(0, numOfNumbers):
    password.append(numbers[random.randint(0, len(numbers) - 1)])

random.shuffle(password)

password = "".join(password)

print(f"Here is your password: {password}")