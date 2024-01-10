year = int(input("enter your year: "))
if year%4==0:
    if year %100 ==0:
        if year%400==0:
            print(f"This {year} is leap")
        else:
            print(f"This {year} not leat")
    else:
        print(f"This {year} is leap")
else:
    print(f"This {year} not leap")
