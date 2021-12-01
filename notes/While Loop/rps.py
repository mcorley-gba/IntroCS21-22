#Rock Paper Scissors

#import random tools
import random 

#create a list of options for the computer to choose:
rps = ['rock', 'paper', 'scissors']

#Flag to keep game running
active_game = True

#Start game loop:
while active_game: #as long as the 'active_game' variable is True, the loop will run
    comp_choice = random.choice(rps)

    #Get player choice
    player_choice = input("\nPlease enter 'rock', 'paper', or 'scissors'. \
\nEnter 'quit' to quit.")

    #Make the player's choice lower case for easy comparison
    player_choice = player_choice.lower()

    #Check if player wants to quit:
    if player_choice == 'quit':
        active_game = False #The player doesn't want to play, no more game
        continue #Will go back to the beginning of the loop,

    #Run through the possible outcomes based on player choice
    elif player_choice == 'rock':
        if comp_choice == 'rock':
            #It's a tie. Tell user:
            print(f"\nIt's a tie! You chose {player_choice}, and the computer chose {comp_choice}.")
        elif comp_choice == 'paper':
            #Computer wins. Tell user:
            print(f"Computer Wins! You chose {player_choice}, and the computer chose {comp_choice}.")
        else: #computer chose scissors
            #Player wins! Tell user:
            print(f"You won! You chose {player_choice}, and the computer chose {comp_choice}.")

    elif player_choice == 'paper':
        if comp_choice == 'rock':
            #Player wins! Tell User:
            print(f"You won! You chose {player_choice}, and the computer chose {comp_choice}.")
        elif comp_choice == 'paper':
            #It's a Tie!
            print(f"\nIt's a tie! You chose {player_choice}, and the computer chose {comp_choice}.")
        else: #Computer chose scissors
            #Computer wins
            print(f"Computer Wins! You chose {player_choice}, and the computer chose {comp_choice}.")

    elif player_choice == 'scissors':
        if comp_choice == 'rock':
            #Computer Wins!
            print(f"Computer Wins! You chose {player_choice}, and the computer chose {comp_choice}.")
        elif comp_choice == 'paper':
            #Player Wins!
            print(f"You won! You chose {player_choice}, and the computer chose {comp_choice}.")
        else: #Computer chose scissors
            #Tie game
            print(f"\nIt's a tie! You chose {player_choice}, and the computer chose {comp_choice}.")

    else: #Capture any input other than the four we've already dealt with
        print(f"Sorry, {player_choice} is not a valid option.")
        continue #restart the loop

    #Game is over, ask if they want to play again
    new_game = input("\nDo you want to play again (yes or no)?")

    #If player doesn't want to play, set flag to False
    if (new_game.lower() != 'yes'):
        active_game = False


