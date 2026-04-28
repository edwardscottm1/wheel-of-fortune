"""
Edward Scott 4/2/26

This program is the main code that is used to simulate 3 rounds of wheel of fortune.
It uses the class defined in wheelOfFortune.py file. This simulate 3 rounds, it does not has
toss ups for the bonus round typically played in wheel of fortune. TO use this code run this program,
it will then print the rules and ask for each users name (you need 3 players or put 3 random names). 
Form their follow the instructions on screen, it uses the same rules as Wheel of Fortune, 
I believe that I didn't forget anything.

This project was hard, it took me lots of try and error to figure out how to tackle certain problems.
I had fun making this project and hope you enjoy using it!

I spent about 20 hours on this code.

Honor Code statement:
I pledge that this program represents my own work. I received help from the python documentation, used the
wheel of fortune website to fact check the rules: https://www.wheeloffortunelive.com/rules,
used this website to get the puzzles:  https://wheeloffortuneanswer.com/#google_vignette,
and used w3schools to lookup and understand some functions that I could use in my program
https://www.w3schools.com/python/default.asp

"""

# Import the module I created
import wheelOfFortuneModule

# Constant that defines how many rounds will be played
NUM_OF_ROUNDS = 3

# Main function
def main():
    # Create a new instance of a class
    WheelOfFortune = wheelOfFortuneModule.wheelOfFortuneGame()

    # Call necessary methods to play wheel of fortune
    # Show rules to user, get contestants names
    WheelOfFortune.printGameRules()
    WheelOfFortune.getPlayerNames()
    WheelOfFortune.getLengthOfPuzzleFile()

    # This loop handles playing multiple rounds
    # Altering the NUM_OF_ROUNDS constant changes the amount of rounds that will be played
    for i in range(NUM_OF_ROUNDS):
        WheelOfFortune.getPuzzleForRound()
        WheelOfFortune.playRound()
        if i < NUM_OF_ROUNDS - 1:
            print('\n\nLet\'s play our next round!\n\n')
    # Methods for winner and farewell
    WheelOfFortune.determineWinner()
    WheelOfFortune.farewell()


# Main function call
if __name__ == '__main__':
    main()