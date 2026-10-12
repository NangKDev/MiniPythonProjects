import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Quit to quit: ").lower()

    if user_input == "Quit".lower():
        break
        
    elif user_input not in options:
        continue
    

    random_number = random.randint(0,2) 
    computer_pick = options[random_number]
    print("Computer picked " + computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")

if user_wins>computer_wins:
    print("Congratulations! You are the winner!")
else:
    print("Computer is the winner. You lost.")



