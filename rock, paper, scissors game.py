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

import random
ascii_hand = [rock, paper, scissors]
user_choice = int(input("State your choice:\nEnter 0 for Rock, 1 for Paper and 2 for Scissors\n"))

computer_choice = int(random.randint(0,3))
if computer_choice == 0:
  print("Computer Choice :\n",ascii_hand[0])
elif computer_choice == 1:
  print("Computer Choice :\n",ascii_hand[1])
else:
  print("Computer Choice :\n",ascii_hand[2])

if user_choice == 0 and computer_choice == 1 :
  print("You Lose!")
elif user_choice == 1 and computer_choice == 0:
  print("You Win!")
elif user_choice == 1 and computer_choice == 2:
  print("You Lose!")
elif user_choice == 2 and computer_choice == 1:
  print("You Win!")
elif user_choice == 2 and computer_choice == 0:
  print("You Lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You Win!")
elif user_choice == computer_choice:
  print("It's a Tie!")
else:
  print("Enter a valid choice")

if user_choice == 0:
  print("Your Choice :\n",ascii_hand[0])
elif user_choice == 1:
  print("Your Choice :\n",ascii_hand[1])
else:
  print("Your Choice :\n",ascii_hand[2])

