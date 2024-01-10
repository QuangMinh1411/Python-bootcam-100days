print("Welcome to Treasure Island. Your misson is to find the treasure")
direction = input("Left or right? ")
if(direction.lower()=="left"):
    action = input("Swim or wait? ")
    if(action.lower()=="wait"):
        door=input("Which door: ")
        if(door.lower()=="yellow"):
            print("You win")
        else:
            print("Game over")
    else:
        print("Game over")
    
else:
    print("Game over")
