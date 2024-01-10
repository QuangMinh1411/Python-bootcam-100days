print("The love calculator your score...")
name1 = input("what your first person: ")
name2 = input("what your second person: ")

combine_name = name1+name2

lower_names = combine_name.lower()
t= lower_names.count("t")
r= lower_names.count("r")
u= lower_names.count("u")
e= lower_names.count("e")

first_digit = t+r+u+e

l= lower_names.count("l")
o= lower_names.count("o")
v= lower_names.count("v")

second_digit = l+o+v+e

score =int(str(first_digit) + str(second_digit))

if(score<10 or score>90):
    print(f"Your score is {score}, you go togethor like coke and mentos.")
elif(score>=40 and score<=50):
    print(f"Your score is {score}, you all right togethor.")
else:
    print(f"Your score is {score}")



