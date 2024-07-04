import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

us_letters = int(input("How many letter would you like in your password\n?"))
us_symbols = int(input("How many symbols would you like\n?"))
us_numbers = int(input("How many numbers would you like\n?"))

password = []

for char in range(1, us_letters+1):
    password.append(random.choice(letters))
for char in range(1,us_symbols+1):
    password.append(random.choice(symbols))
for char in range(1,us_numbers+1):
    password.append(random.choice(numbers))
    
random.shuffle(password)

password_str = ''.join(password)

print(password_str)

