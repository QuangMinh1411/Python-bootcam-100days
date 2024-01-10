# # two_digit_num = input()
# # first_digit = int(two_digit_num[0])
# # second_digit = int(two_digit_num[1])
# # two_digit_num = first_digit+second_digit
# # print(two_digit_num)

# score = 9
# height=1.65
# isWinning = True

# #f-String

# print(f"your score is {score} ,your height is {height}-you are {isWinning}")

# age = input("Your age: ")
# years = 90- int(age)
# weeks= years*52;
# print(f"You have {weeks}")

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?$"))
percent= int(input("what percentage you tip?10,12 or 15:"))
people = int(input("How many people you have?"))
bill_with_tip = percent/100*total_bill+total_bill
print(f"Tip each person: ${round(bill_with_tip/people,2)}")