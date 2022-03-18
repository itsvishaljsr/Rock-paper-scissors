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

user_choosen = int(input("Enter 1 for Rock, 2 for Paper and 3 for Scissors: "))
computer_choosen = random.randint(1, 3)

if user_choosen < computer_choosen:
    if computer_choosen == 2:
        print(f"You chose:\n {rock}\nComputer chose:\n{paper}\nYOU LOSE")
    if computer_choosen == 3 :
        print(f"You chose:\n {rock}\nComputer chose:\n{scissors}\nYOU WIN")
elif user_choosen > computer_choosen :
    if computer_choosen == 1:
        print(f"You chose:\n {paper}\nComputer chose:\n{rock}\nYOU WIN")
    if computer_choosen == 2 :
        print(f"You chose:\n {scissors}\nComputer chose:\n{paper}\nYOU WIN")
else :
  if user_choosen == computer_choosen == 1 :
    print(f"You chose:\n {rock}\nComputer chose:\n{rock}\nDRAW")
  if user_choosen == computer_choosen == 2 :
    print(f"You chose:\n {paper}\nComputer chose:\n{paper}\nDRAW")
  if user_choosen == computer_choosen == 3 :
    print(f"You chose:\n {scissors}\nComputer chose:\n{scissors}\nDRAW")