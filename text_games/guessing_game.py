#guessing_game.py
#Simple number guessing game
#The Computer will think of a number 
#and the player will try to guess it

#import python's random abilities
import random #random is a built-in library of functions and methods

#Set game flag
active_game = True

#Main game loop
while active_game: #As long as the active_game flag is True, the game will run
    
    #Have the computer "choose" a number:
    comp_choice = random.randint(1,100) #Generate a random number between 1 and 100 (inclusive)

    #Tell user a number has been chosen
    print("I'm thinking of a number between 1 and 100.")
    
    #Set flag for player choice correctness:
    correct = False

    #Loop for continuous choosing
    while not correct: #As long as correct is False, 'not correct' will be True, 
                        #and the loop will run.
        #Get the player's guess:
        player_guess = input("\nGuess a number or enter 'quit' to end the game: ")

        #If player says 'quit', we need to exit the guessing loop
        if player_guess.lower() == 'quit':
            break #exits the guessing loop
        else:
            #Player entered a number, turn it into an integer for comparison
            player_guess = eval(player_guess)
        
        #Compare player guess to computer choice:
        if player_guess > comp_choice:
            #Player guessed too high. Let them know.
            print(f"\nToo high! {player_guess} was too high.")
            #No need to change correct flag, because player was wrong
        elif player_guess < comp_choice:
            #Player guessed too low. Let them know:
            print(f"\nToo low! {player_guess} was too low.")
            #No need to change the correct flag, because the player was wrong
        else: #player_guess == comp_choice
            #Player is correct! Tell them:
            print(f"Congratulations! {player_guess} was correct!")
            #Change correct to True because player got it right
            correct = True #now, 'not correct' is False and the guessing loop will close

    #If guessing loop exited because of a good guess, ask if another game is wanted
    if correct: #If the correct flag is True, the user guesssed right, 
                #do they want to play again?
        new_game = input("\nDo you want to play again (yes or no)? ")
    
    #If guessing loop ended because the user entered quit
    #or if user was correct but said no to new_game question
    #Then we need to stop the game.
    if (correct == False) or (new_game.lower() == 'no'):
        #If player entered 'quit' or entered 'no' for new_game, 
        #set active_game to False to close the game.
        active_game = False

        #Why do we HAVE TO check the correct flag before the new_game value?

