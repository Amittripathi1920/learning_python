import random

Rock = ''' Rock
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''

Paper = ''' Paper
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________) 
  '''

Scissors = ''' Scissors
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  '''

options = [Rock, Paper, Scissors]

user_selection = int(input("Please Select 0 for Rock, 1 for Paper or 2 for Scissors. :"))

if user_selection >= 0 and user_selection <= 2:
    print(f"****************************************************************\nYour Selection : \n{options[user_selection]}")
    computer_selection = random.randint(0,2)
    print(f"Computer Selection : \n{options[computer_selection]}")
    if user_selection == 0 and computer_selection == 2:
        print("You Win")
    elif user_selection == 2 and computer_selection == 0:
        print("You Loose")
    elif user_selection > computer_selection:
        print("You Win")
    elif user_selection < computer_selection:
        print("You Loose")
    elif user_selection == computer_selection:
        print("It's Draw")
    else:
        print("I'm Confused :( ")
else:
    print("Please Select one valid Option :- 0 for Rock, 1 for Paper or 2 for Scissors\n****************************************************************\n")
