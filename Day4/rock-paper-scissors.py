import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,len(game_images)-1)
print(game_images[human_choice])
    
print(f"Computer chose:\n {game_images[computer_choice]}")
if human_choice>=3 and human_choice<=0:
    print("You typed invalid number, you lose")
elif human_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice==0 and human_choice==2:
    print("You lose")
elif computer_choice>human_choice:
    print("You lose")
elif computer_choice<human_choice:
    print("You win")
else:
    print("Deuce")
    

