# **Pig Game is a game where a group of players (at least 2) take turn on rolling a die, and each time they roll, the number on the die adds up to their score. However, if number 1 is rolled, the player lose all the score of that round (only the score up to previous round remain). The first person to reach the max score, wins.
#You need to end the game if you think your score is over the max score! Or else once you roll 1, you will lose all the score for that round.
#The code written here lets the last player number to finish even if the previous player won already. 

import random

#def function to define number of die rolls between 1 and 6
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

#input number of players which must be a valid integer between 2 and 4
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

# initializing a total score list of each player ,example: [0,0,0] for three players
max_score =  50
player_scores = [0 for _ in range(players)] #a list of scores of each player

while max(player_scores) < max_score:

    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "turn has just started!") #Adding one to the player_index as index starts from 0
        print("Your total score is:", player_scores[player_index], "\n")

        current_score = 0
        while True:
            #ask the player if they want to roll

            should_roll = input("Would you like to roll? (Press y if yes & anything if no): ")
            if should_roll.lower() != "y":
                break

            #ends when the player rolls 1 and add the score if other number is rolled   
            value = roll()
            if value == 1:
                print("You rolled a 1!. Your turn is done!")
                current_score = 0
                break

            else:
                current_score += value
                print("You rolled a", value)

            print("Your current score is:", current_score) #the score for each round, which is different from overall total score of all the rounds ** once number one is rolled, this score will be 0 so only the player_scores[player_index] remains

        player_scores[player_index] += current_score
        print("Your TOTAL SCORE is:", player_scores[player_index]) #Total score of each player

max_score = max(player_scores)
winning_idx = player_scores.index(max_score) #search the index of the max score
print("Player number", winning_idx + 1, "is the winner with a score of", max_score) #index starts from 0 