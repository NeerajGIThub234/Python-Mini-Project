import random

#to generate random value for a die between 1 to 6
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# to get the no of players between 1 to 4
while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
#list comprehension make a list according to no of players and gave each players score 0
player_scores = [0 for _ in range(players)] 

while max(player_scores) < max_score:    # chechk that every player score is not more than max score
    for player_idx in range(players):    # started player turn one by one
           print("\nPlayer number",player_idx + 1, "turn has just started!\n")
           print("Your total score is:", player_scores[player_idx],"\n")
           current_score = 0

           while True:
              should_roll = input("Would you like to roll (y)? ")
              if should_roll.lower() != "y":  #if player not role 
                break

              value = roll()
              if value == 1:   # if player roll and get 1
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
              else:
                current_score += value
                print("You rolled a:", value)

              print("Your Score is:", current_score ,"\n")
        
           player_scores[player_idx] += current_score  # fix the player score in list
           print("Your total score is:", player_scores[player_idx],"\n")

# who win the game 
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
                 
        


