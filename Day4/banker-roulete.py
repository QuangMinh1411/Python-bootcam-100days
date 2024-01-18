import random
name_string = input("enter your list name: ")
names = name_string.split(", ")
random_choice = random.randint(0,len(names)-1)

print(f"person will pay the bill is {names[random_choice]}")
