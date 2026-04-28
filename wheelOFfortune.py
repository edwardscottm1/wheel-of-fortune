"""
Edward Scott 4/28/26

This program is contains a class that is used to play a round of wheel of fortune. 
It has methods to get each player's name, get a puzzle for a round, generate a wheel with values,
spin the wheel, play a round of wheel of fortune and other methods used to handle the game logic.
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

# Import needed modules
import random
import time

# Class used for wheel of fortune logic
class wheelOfFortuneGame:
    # Create needed constants
    INPUT_FIELD = '>> ' 
    BORDER_LENGTH = 100
    # The time module has a function to stop program flow (sleep), I used this to allow players to read the output
    # in the console then have the next part of the game print
    # Without this module it would be hard for players to keep track of what is happening
    SHORT_PAUSE = 1
    MEDIUM_PAUSE = 2
    LONG_PAUSE = 4

    # Constants for letters
    VOWELS = ('A', 'E', 'U', 'I', 'O')
    CONSONANTS = ('Q', 'W', 'R', 'T', 'Y', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M')
    
    # Initialise needed attributes
    def __init__(self):
        
        self.__puzzleForRound = {'category': '', 'text': []}
        self.__puzzleAsBlankChars = []
        self.__vowelsInPuzzle = []
        self.__vowelsRevealed = False
        self.__scores = [ # placeholder values THIS NEED TO BE SET TO NOTHING WHEN DONE
            {'user':'Edward', 'money': 0},
            {'user':'Elliott', 'money': 0},
            {'user':'Alex', 'money': 0}
        ]
        self.__numberOfLines = 0
        self.__wheelValues = []

    # Method used to print the game rules and title, NOT COMPLETE
    def printGameRules(self):
        # print('=' * self.BORDER_LENGTH)
        # print('Wheel of Fortune'.center(self.BORDER_LENGTH))
        # print('=' * self.BORDER_LENGTH)
        print()
        print(" ■           ■  ■       ■  ■ ■ ■ ■  ■ ■ ■ ■  ■          ■ ■ ■   ■ ■ ■ ■ ")
        print("  ■         ■   ■       ■  ■        ■        ■         ■     ■  ■       ")
        print("   ■   ■   ■    ■ ■ ■ ■ ■  ■ ■ ■ ■  ■ ■ ■ ■  ■         ■     ■  ■ ■ ■ ■ ")
        print("    ■ ■ ■ ■     ■       ■  ■        ■        ■         ■     ■  ■       ")
        print("     ■   ■      ■       ■  ■ ■ ■ ■  ■ ■ ■ ■  ■ ■ ■ ■    ■ ■ ■   ■       ")
        print()
        print("     ■ ■ ■ ■   ■ ■ ■   ■ ■ ■  ■ ■ ■ ■ ■  ■     ■  ■     ■  ■ ■ ■ ■")
        print("     ■        ■     ■  ■    ■     ■      ■     ■  ■ ■   ■  ■      ")
        print("     ■ ■ ■ ■  ■     ■  ■ ■ ■      ■      ■     ■  ■  ■  ■  ■ ■ ■ ■")
        print("     ■        ■     ■  ■  ■       ■      ■     ■  ■   ■ ■  ■      ")
        print("     ■         ■ ■ ■   ■   ■      ■       ■ ■ ■   ■     ■  ■ ■ ■ ■")
        time.sleep(self.MEDIUM_PAUSE)
        print('\nWelcome to tonights shows folks, I\'m your host Jim Thornton. If you are new to the show here are the rules:\n')
            
        print('\n1. A puzzle and category will be revealed to users, the puzzle will be a bunch of blank characters, as users ') 
        print('\t\tguess the letters the puzzle will be revealed. The round ends once a user solves the puzzle.') 

        print('\n2. Each player will have a grand total and sub total during the round,')
        print('\t-- The total during the round is the money earned by guessing correct consonants. The user keeps this total if they solve ')
        print('\t\tthe puzzle correct, then it will be added to their grand total') 
        print('\t-- After 3 rounds of play, the grand total is used to determine the winner')
    
        print('\n3. Each player will take turns spinning the wheel during the round,')        
        print('\t-- Land on BANKRUPT, the player loses the money earned from the round and their turn ends')
        print('\t-- Land on LOSE TURN, the player turn\'s end and the next player gets to spin the wheel')
        print('\t-- Land on money, the player then can guess a consonant, buy a vowel, or solve the puzzle.') 
        print('\t\tThis value is used to determine how much money they can earn')
    
        print('\n4. When a player guesses a consonant,')
        print('\t-- The player will be prompted to enter a consonant they think is in the puzzle')
        print('\t-- If the consonant is in puzzle, the consonant will be revealed in the puzzle, and the number of instance of') 
        print('\t\tthe consonant in the puzzle times the landed value will equal how much money the user earns for that guess.') 
        print('\t\tThe user then can spin the wheel again')
        print('\t-- If the consonant is not in the puzzle, the player will lose their turn')
        print('\t-- If the users guesses a consonant that was already guessed, the player will lose their turn')
        
        print('\n5. When a user buys a vowel,')
        print('\t-- The user will be prompted to enter a vowel they wish to buy')
        print('\t-- Each vowel cost $250, each time a player buys a vowel $250 will be subtracted from their total in the current round')
        print('\t-- If the vowel is not in puzzle, if the vowel is not in the puzzle, the player\'s turn ends')
        print('\t-- If the vowel is in the puzzle, the vowel will be shown in the puzzle, the player can buy another vowel if they wish,')
        print('\t\tafter buying vowels the player can either guess a consonant or solve the puzzle')

        print('\n6. When user wants to solve the puzzle,')
        print('\t-- The player will be prompted to enter the puzzle correctly')
        print('\t-- If entered correctly, the round ends and the money earned by the player that solves the puzzle will be added to their')
        print('\t\tgrand total.')
        print('\t-- If entered incorrectly, the player loses their turn and the next player spins the wheel')
    
        print('\n7. After 3 rounds of play a winner is determined,')
        print('\t-- The player with the most amount of money earned will be the winner')
        print('\t-- In the rare instance of a tie, the tied players will play rock paper scissors to determine the winner')
        time.sleep(self.LONG_PAUSE)


    # Method used to get names of players
    def getPlayerNames(self):
        print('\nLet\'s see who will be playing Wheel of Fortune tonight!\n')
        print('Please enter the names for the players playing')
        for i in range(3):
            # Ensure user enters a name, not just a space
            inputValid = False
            while not inputValid:
                userInput = input(f'Player {i + 1} name\n{self.INPUT_FIELD}').upper().rstrip()
                if userInput == ' ' or userInput == '':
                    print('Please enter a name')
                    continue
                self.__scores[i]['user'] = userInput
                inputValid = True
                
            
        print('\nOkay contestants, let\'s play our first round')
    
    # Method used to get length of puzzles file, this is done to allow users to add more puzzles to the file (if they want to) 
    # and have program not crash
    def getLengthOfPuzzleFile(self):
        with open('puzzles.txt', 'r') as puzzlesFile:
            # List comprehension, we go over each line in the file and get a value of 1, to get the 
            # number of lines in the file
            self.__numberOfLines = sum([1 for line in puzzlesFile])
                    
    # Method used to get a random puzzle from the puzzles file
    def getPuzzleForRound(self):
        # Get a random integer, this will be the random line in the file
        randomLine = random.randint(1, self.__numberOfLines)
        
        # Variable to store puzzle 
        puzzle = ''
        # Read the file 
        with open('puzzles.txt', 'r') as puzzlesFile:
            for i in range(randomLine):
                puzzle = puzzlesFile.readline()
            # Once puzzle found, split it to category and puzzle
            puzzle = puzzle.rstrip('\n').split('-')
            

        # Save to the appropriate attributes
        self.__puzzleForRound['category'] = puzzle[0]
        self.__puzzleForRound['text'] = puzzle[1].upper()

        # Make a version of the puzzle as blank characters to show to players during the game    
        # Each word becomes a row of equal signs 
        self.__puzzleAsBlankChars = ['=' * len(word) for word in self.__puzzleForRound['text'].split()]

        # This is used to keep track of vowels in the puzzle. 
        # Used to check when players bought every vowel
        # First we clear the attribute in case any vowels were left over from previous rounds
        self.__vowelsInPuzzle.clear()
        # Then we loop through the vowels in the VOWELS constant tuple
        for vowel in self.VOWELS:
            # If the word contains the vowel, we append the vowel to the __vowelsInPuzzle attribute
            if vowel in self.__puzzleForRound['text']:
                self.__vowelsInPuzzle.append(vowel)

    # Method used to print the scores from each player
    def displayScores(self, scores, title):
        print(f'\n{title}')
        for i in range(len(scores)):
            print(f'{scores[i]['user']:^10}\t', end = '')
        print()
        for i in range(len(self.__scores)):
            print(f'${scores[i]['money']:^10.2f}\t', end = '')
        print()
    
    # Method used to generates values for the wheel for the round
    def generateValuesForWheel(self):
        self.__wheelValues = random.choices(range(500, 1500, 100), k = 8)
        # In wheel of fortune there are wedges on the wheel to make players lose their turn or all their money
        self.__wheelValues.insert(random.randint(0, len(self.__wheelValues)), 'BANKRUPT')
        self.__wheelValues.insert(random.randint(0, len(self.__wheelValues)), 'LOSE YOUR TURN')

    # Method used to spin the wheel, takes a list of values that are on the wheel
    def spinWheel(self, values):
        # Constant for how many times we loop over the wheel
        NUM_OF_CYCLES = 2
        SHORT_PAUSE = .08
        LONG_PAUSE = .3

        # This determines which value the user lands on the wheel
        # The index to stop the "spin"
        endingIndex = random.randint(1, len(values))

        # Variable used to return the value the user landed on
        landedValue = None
        
        # Loop used to loop over the list of values and show it like a spinning wheel almost
        for i in range(NUM_OF_CYCLES):
                for i in range(len(values)):
                    print(f'--{values[i]:^16}--', end = '\r')
                    time.sleep(SHORT_PAUSE)
        # After "two cycles of the wheel" it slows down to a value determined by the endingIndex
        for i in range(endingIndex):
            print(f'--{values[i]:^16}--', end = '\r')
            time.sleep(LONG_PAUSE)
            # Save the landed value
            landedValue = values[i]
        print()
                
        return landedValue

    # Method used to play a round of wheel of fortune 
    def playRound(self):
        # Print a introductory message
        print(f'The category for this round is: {self.__puzzleForRound['category']}')
        time.sleep(self.MEDIUM_PAUSE)

        # Generate the values for the wheel for this round
        self.generateValuesForWheel()
        self.printListInLine(self.__wheelValues, 'The values on the wheel are')

        # List used to store the money earned in the round
        scoresCurrentRound = [
            {'user': self.__scores[0]['user'], 'money': 0},
            {'user': self.__scores[1]['user'], 'money': 0},
            {'user': self.__scores[2]['user'], 'money': 0},
        ]

        # Sentinel variable used to keep round going till the puzzle is solved
        puzzleSolved = False

        # Create sets to store consonant and vowels guessed/purchased
        guessedConsonants = set()
        purchasedVowels = set()
        self.__vowelsRevealed = False
        # Loop to play game, each player takes turn to spin wheel and guess the letters of the puzzle
        while not puzzleSolved:
            
            # Loop through scoresCurrentRound list, to let each player play
            for player in range(len(scoresCurrentRound)):
                # Sentinel variable used to keep track if a player's turn is over
                # It ends when they guess a consonant, vowel or the puzzle wrong or when they land on lose turn or bankrupt
                turnOver = False
                while not turnOver:
                    # At start of each turn print the money each player has
                    self.displayScores(scoresCurrentRound, 'Current Scores:')
                    
                    # Show the current puzzle as blank characters, to user
                    # This gets filled in with letters as the players guess the letters
                    print('\nHere is your puzzle')
                    print(' '.join(self.__puzzleAsBlankChars))
                    
                    # Show the guessed consonants and bought vowels
                    self.printListInLine(guessedConsonants, 'Guessed Consonants')
                    self.printListInLine(purchasedVowels, 'Purchased Vowels')
                    
                    # Let user spin the wheel
                    print(f'\n{scoresCurrentRound[player]['user']} it is your turn, press "enter" to spin the wheel!')
                    input(self.INPUT_FIELD)
                    landedValue = self.spinWheel(self.__wheelValues)
                    
                    # If user lands on BANKRUPT, they lose their money and their turn
                    if landedValue == 'BANKRUPT':
                        print('\nYou landed on BANKRUPT')
                        print('Whoops, you lost all your money and your turn!\n')
                        scoresCurrentRound[player]['money'] = 0
                        turnOver = True
                        time.sleep(self.MEDIUM_PAUSE)
                        continue
                    # If user lands on LOSE YOUR TURN, their turn ends
                    elif landedValue == 'LOSE YOUR TURN':
                        print('\nYou landed on LOSE YOUR TURN')
                        print('Whoops, you lost your turn!\n')
                        turnOver = True
                        time.sleep(self.MEDIUM_PAUSE)
                        continue
                    else:
                        # Inform user what they landed on 
                        print(f'\nYou landed on ${landedValue}\n')
                        time.sleep(self.MEDIUM_PAUSE)
                    
                    # Ask user on what they would like to do
                    # If all the vowels have been revealed, we remove the vowel option
                    if self.__vowelsRevealed == False:
                        userInput = self.handleMenuSelection(['Guess consonant', 'Solve the puzzle', 'Buy a vowel'])
                    else:
                        userInput = self.handleMenuSelection(['Guess consonant', 'Solve the puzzle'])

                    # Call the appropriate method based on user input
                    # The turnOver variable will gets a new boolean value to determine if the players
                    # turn is over or not
                    if userInput == 1:
                        turnOver = self.playerGuessesConsonant(landedValue, guessedConsonants, player, scoresCurrentRound)
                    elif userInput == 2:
                        # If solved we set the sentinel variables to their appropriate values to exit the loop
                        # and store which player solved the puzzle
                        turnOver, puzzleSolved, player = self.playerSolvePuzzle(player)
                    elif userInput == 3:
                        turnOver = self.playerBuysVowel(purchasedVowels, player, scoresCurrentRound)
                        if turnOver:
                            continue
                        # After buying vowels, the user can either guess a consonant or solve the puzzle
                        userInput = self.handleMenuSelection(['Guess a consonant', 'Solve the puzzle'])
                        if userInput == 1:
                            turnOver = self.playerGuessesConsonant(landedValue, guessedConsonants, player, scoresCurrentRound)
                        elif userInput == 2:
                            turnOver, puzzleSolved, player = self.playerSolvePuzzle(player)
                
                # When puzzle is solved, we break out of the game loop        
                if puzzleSolved: 
                    break
        # After puzzle solved inform players and add the money earned for the player that solved the puzzle
        print('\nRound over')
        print(f'Great job {scoresCurrentRound[player]['user']}! The money earned from this round will be added to your total.')
        self.__scores[player]['money'] += scoresCurrentRound[player]['money']
        self.displayScores(self.__scores, 'Scores after the puzzle:')
        time.sleep(self.LONG_PAUSE)               

    # Method used to handle user wanting to guess a consonant in the puzzle
    def playerGuessesConsonant(self, landedValue, guessedConsonants, player, scores):
        # Print the puzzle and the guessed consonants
        print(f'\nPuzzle:\n{' '.join(self.__puzzleAsBlankChars)}')
        self.printListInLine(guessedConsonants, 'Guessed Consonants')
        
        # Ask user to enter a consonant
        validInput = False
        while not validInput:
            userInput = input(f'\nGuess a consonant in the puzzle\n{self.INPUT_FIELD}').upper().rstrip()
            # Check to see if user entered a consonant, if not they will be asked to enter a letter again
            if userInput not in self.CONSONANTS:
                validInput = False
                print('Please enter a consonant')
                continue
            validInput = True
        else:
            # We need to check that they entered a character that has already been guessed, if it is their turn ends
            if userInput in guessedConsonants:
                print(f'\nSorry, "{userInput}" was already guessed, you turn has ended.')
                time.sleep(self.SHORT_PAUSE)
                return True

        # Once user enters a consonant, we keep track of constants guessed
        guessedConsonants.add(userInput)

        # Check to see how many instances of the user entered consonant is in the puzzle
        num = self.checkForCharInPuzzle(self.__puzzleForRound['text'], userInput)
        
        # Based on the number of instances of the consonant, print an appropriate message
        # If the consonant is in the puzzle, we need to update the list that stores the puzzle
        # with blank characters
        if num > 1:
            print(f'\nThere are {num} "{userInput}"s!')
            self.replaceBlankStrWithChars(userInput)
        elif num == 1:
            print(f'\nThere is 1 "{userInput}"')
            self.replaceBlankStrWithChars(userInput)
        else:
            # When player does not get any characters correct, their turn ends
            print(f'\nSorry there are no "{userInput}"s in the puzzle. Next players turn.')
            time.sleep(self.SHORT_PAUSE)
            return True
            
        # Add user score
        # This depends on the number of instance of the letter times the number the user landed on with the wheel
        print(f'Money earned: {num * landedValue}')
        scores[player]['money'] += num * landedValue
        time.sleep(self.SHORT_PAUSE)
        # Return false to allow user to spin again since they guesses correctly
        return False

    # Method used to allow user to purchase a vowel
    def playerBuysVowel(self, purchasedVowels, player, scores):
        # Cost of a vowel
        VOWEL_COST = 250

        # Sentinel variable to allow user purchase another vowel
        # Loop till user does not want to buy another vowel, or they cannot buy another one
        buyAnother = 'Y'
        while buyAnother == 'Y':
            # Print user their balance and the cost of a vowel
            print(f'\nYour balance: ${scores[player]['money']:.2f}\t\t Cost of vowel: {VOWEL_COST}')
            # First check if user has enough money to buy a vowel
            if scores[player]['money'] < VOWEL_COST:
                print('Sorry, you don\'t have enough money to buy a vowel\n')
                time.sleep(self.SHORT_PAUSE)
                break # stop the loop

            # Print the puzzle with blank characters and the purchases vowels
            print(f'\nPuzzle:\n{' '.join(self.__puzzleAsBlankChars)}')
            self.printListInLine(purchasedVowels, 'Purchased Vowels')

            # Ask user to enter a vowel
            validInput = False
            # Loop till user enters a valid input
            while not validInput:
                userInput = input(f'\nWhich vowel would you like to buy?\n{self.INPUT_FIELD}').upper().rstrip()
                # Check if user entered nothing or if they entered a consonant
                # If so the user needs to enter a vowel to continue
                if userInput not in self.VOWELS:
                    validInput = False
                    print('Please buy a vowel!\n')
                    continue
                # If input valid, set sentinel variable to true
                validInput = True
            else:
                # After player enters a vowel, we check to see if the vowel was bought already 
                # If it was, their turn is over
                if userInput in purchasedVowels:
                    print(f'\nSorry, "{userInput}" was already purchases, you turn has ended.\n')
                    time.sleep(self.SHORT_PAUSE)
                    return True
            

            # Keep track of vowels purchases
            purchasedVowels.add(userInput)

            # Subtract cost of vowel to player's balance
            scores[player]['money'] -= VOWEL_COST 

            # Check to see how many of the purchased vowel are in the puzzle
            num = self.checkForCharInPuzzle(self.__puzzleForRound['text'], userInput)
            
            # Display appropriate message based on number of vowels in the puzzle
            if num == 0:
                print(f'Sorry there is no "{userInput}"s in the puzzle. Your turn ends\n')
                time.sleep(self.SHORT_PAUSE)
                # Exit the function, when player buys a vowel not in the puzzle, their turn ends
                return True
            elif num > 1: 
                print(f'\nThere are {num} "{userInput}"s in the puzzle')
                self.replaceBlankStrWithChars(userInput)
                print(f'\nPuzzle:\n{' '.join(self.__puzzleAsBlankChars)}')
                time.sleep(self.SHORT_PAUSE)
            else: 
                print(f'\nThere is 1 "{userInput}" in the puzzle')
                self.replaceBlankStrWithChars(userInput)
                print(f'\nPuzzle:\n{' '.join(self.__puzzleAsBlankChars)}')
                time.sleep(self.SHORT_PAUSE)

            # We remove the vowel from this list to keep track of vowels not revealed yet
            self.__vowelsInPuzzle.remove(userInput)
            
            # Once all the vowels have been bought, we inform players of it
            if len(self.__vowelsInPuzzle) == 0:
                print('No more vowels left to buy!\n')
                self.__vowelsRevealed = True
                time.sleep(self.SHORT_PAUSE)
                break # Exit loop to allow player to guess consonant or solve puzzle

            # Ask user if they would like to buy another vowel
            print(f'\nYour balance: ${scores[player]['money']:.2f}')
            buyAnother = input(f'\nWould you like to buy another vowel? (Y?)\n{self.INPUT_FIELD}').upper()
            print()

        
        # We exit this method once user can't or won't buy another vowel
        return False
    
    # Method used to handle players solving the puzzle
    def playerSolvePuzzle(self, player):
        # Show the partially solved puzzle and prompt user for guess
        print(f'\nPuzzle:\n{' '.join(self.__puzzleAsBlankChars)}')
        print('\nType the puzzle word for word (no extra spaces please!):')
        userInput = input(self.INPUT_FIELD).rstrip().upper()

        if userInput == self.__puzzleForRound['text']:
            # If guess correct, inform players, return boolean values to exit loop and player who solved it 
            print(f'Correct! the puzzle was: {self.__puzzleForRound['text']}')
            time.sleep(self.SHORT_PAUSE)
            return True, True, player
        else:
            # If guess incorrect, current players turn is over
            print('Wrong, next players turn!')
            time.sleep(self.SHORT_PAUSE)
            return True, False, None
            
    # Method used to check if a character entered by the player is in the puzzle
    # It returns an int of how many instances of the character is in the puzzle
    def checkForCharInPuzzle(self, puzzle, char):
        return puzzle.count(char)
        
    # Method used to replace blank characters in puzzle to correct guessed/purchases characters
    def replaceBlankStrWithChars(self, userInput):
        # Variable used to keep track of the words index in the __puzzleAsBlankChars list
        wordIndex = 0
    
        # Loop through each word in the puzzle for the round
        for word in self.__puzzleForRound['text'].split():
            # Variable used to keep track of the current characters index
            charIndex = 0
            # Loop through every character in the word
            for char in word:                
                # If the character equals the character the user entered, we replace the blank character in __puzzleAsBlankChars
                # with the appropriate letter
                if char == userInput:    
                    # In order to replace the character, we slice the string. 
                    # First we slice the string from the start to the character before the one that needs to be replaced
                    # Then we concatenate the letter the user entered to the first slice
                    # Then slice the original string to get the rest of the string and concatenate it to the previous strings
                    self.__puzzleAsBlankChars[wordIndex] = self.__puzzleAsBlankChars[wordIndex][:charIndex] + userInput + self.__puzzleAsBlankChars[wordIndex][charIndex + 1:]
                
                # Increment the variables
                charIndex += 1
            wordIndex += 1

    # Method used to print a list/set in a row with a title
    def printListInLine(self, items, title):
            print(f'\n{title}:')
            count = 0
            for item in items:
                if count < len(items) - 1:
                    print(f'{item} | ', end = '')
                else:
                    print(item)

                count += 1
            print()


    # Method that takes a list as an argument to generate a menu selection screen
    # This method handles invalid inputs also
    def handleMenuSelection(self, options):
        # Ensure input is valid
        inputValid = False
        while not inputValid:
            try:
                # Print the menu of options
                print('Choose from the options below:')
                for i in range(len(options)):
                    print(f'{i + 1}. {options[i]}')
                    
                userInput = int(input(self.INPUT_FIELD))
                # Check to see number entered is in range
                if userInput > 0 and userInput <= len(options):
                    inputValid = True
                    return userInput
                else:
                    print('\nPlease enter a valid option')
            # In case user enters anything other than a int
            except ValueError:
                print('\nPlease enter a valid option')
        
    # Method used to determine a winner after playing three rounds
    def determineWinner(self):
        # Create variables to store who was the winner, how much money they win, and a list to store players that tied
        winner = ''
        highestScore = 0 # stores the money earned by the winner
        tiedPlayers = []
        # Loop through every player in the scores attribute
        for player in self.__scores:
            # Save the highest score and its associated player
            if player['money'] > highestScore:
                winner = player['user']
                highestScore = player['money']
            # If multiple players have the highest score, we store their names in the tiedPlayers list
            elif highestScore == player['money']:
                tiedPlayers.append(player['user'])
                # in case we appended a player to the list already, we make sure to not append them twice
                if winner not in tiedPlayers:
                    tiedPlayers.append(winner)
        
        # Print message to inform users of game ending
        print('\n\nLet\'s see the who is our winner')
        time.sleep(self.SHORT_PAUSE)
        
        # If there is a tie, inform players of it
        if len(tiedPlayers) > 0:
            print('There\'s a tie between:', ', '.join(tiedPlayers))
            print('Play again to determine a winner or play rock papers scissors shoot!')
        else:
            # Congratulate winner
            print(f'Congrats {winner} you won ${highestScore:,}')
        time.sleep(self.MEDIUM_PAUSE)
            

    # Method used to say goodbye and thank you to the players after playing 3 rounds
    def farewell(self):
        print('\n\nThank you for your time and for playing Wheel of Fortune!')
        print('I hope you can join us again next night for another show.')
        print('Have a good night folks!')
