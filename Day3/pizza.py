print("Thank you choosing Pizza")
size=input("What size pizza you choose?S,M or L: ")
add_pepperoni = input("Do you want pepperoni?Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
print("Thank you for choosing Pizza delivery")
bill = 0
pepperoni = 0
cheese = 0
if(size=="S"):
    bill=15
    if(add_pepperoni=="Y"):
        pepperoni=2
    if(extra_cheese=="Y"):
        cheese=1
elif (size=="M"):
    bill=20
    if(add_pepperoni=="Y"):
        pepperoni=3
    if(extra_cheese=="Y"):
        cheese=1
else:
    bill = 25
    if(add_pepperoni=="Y"):
        pepperoni=3
    if(extra_cheese=="Y"):
        cheese=1
print(f"Your final bill is: ${bill+pepperoni+cheese}")
    
    