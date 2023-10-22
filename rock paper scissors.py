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

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice! You Lose!")
else:
    print("You Chose:")
    print(game_images[user_choice])
    
    pc_choice = random.randint(0, 2)
    print("PC chose:")
    print(game_images[pc_choice])

    if user_choice == pc_choice:
        print("It's a draw!")
    elif (user_choice == 0 and pc_choice == 2) or (user_choice == 1 and pc_choice == 0) or (user_choice == 2 and pc_choice == 1):
        print("You win!")
    else:
        print("You lose!")
