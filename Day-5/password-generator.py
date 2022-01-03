#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

unordered_password = []
password = []

for num in range(0, nr_letters):
  unordered_password.append(random.choice(letters))

for num in range(0, nr_symbols):
  unordered_password.append(random.choice(numbers))

for num in range(0, nr_numbers):
  unordered_password.append(random.choice(symbols))

temp = ''
for character in unordered_password:
  temp += character

for num in range(0, len(unordered_password)):
  random_letter = random.choice(unordered_password)
  unordered_password.remove(random_letter)
  password.append(random_letter)
  
temp2 = ''
for character in password:
  temp2 += character

print(f'''\nYour non-randomised password is: {temp}
Your random password is: {temp2}''')

