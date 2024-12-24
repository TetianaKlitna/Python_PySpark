import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
cntLetters = int(input("How many letters would you like in the password?\n"))
cntSymbols = int(input("How many symbols would you like?\n"))
cntNumbers = int(input("How many numbers would you like?\n"))
sizePassword = cntLetters + cntSymbols + cntNumbers

passwordList = []
for ind in range(0, cntLetters):
    passwordList.append(random.choice(letters))

for ind in range(0, cntSymbols):
    passwordList.append(random.choice(symbols))

for ind in range(0, cntNumbers):
    passwordList.append(random.choice(numbers))

random.shuffle(passwordList)
password = "".join(passwordList)

print(password)
