#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# My solution
# list_letter = []
# list_symbol = []
# list_number = []
# password = []
# hardpass=[]
# for i in range(0,nr_letters):
#     list_letter.append(letters[random.randint(0,len(letters)-1)])
# for i in range(0,nr_symbols):
#     list_symbol.append(symbols[random.randint(0,len(symbols)-1)])
# for i in range(0,nr_numbers):
#     list_number.append(numbers[random.randint(0,len(numbers)-1)])

# for i in range(0,nr_letters+nr_numbers+nr_symbols):
#     if i<nr_letters:
#         password.append(list_letter[i])
#     elif i<nr_letters+nr_numbers:
#         password.append(list_symbol[i-nr_letters])
#     else:
#         password.append(list_number[i-nr_letters-nr_symbols])
        
# print(f"Your simple password is {''.join(password)}")
# length = len(password)
# for i in range(0,length):
#     index = random.randint(0,len(password)-1)
#     hardpass.append(password[index])
#     password.pop(index)
# print(f"Your hard password : {''.join(hardpass)}")

password_list = []
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))
for char in range(0,nr_symbols):
    password_list+=random.choice(symbols)
for char in range(0,nr_numbers):
    password_list+=random.choice(numbers)

random.shuffle(password_list)
print(f"Your password is {''.join(password_list)}")

