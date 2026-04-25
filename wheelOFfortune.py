'''This file will contain the class used to play the wheel of fortune game'''
# 3 hours

import random
import time

class wheelOfFortuneGame:
    INPUT_FIELD = '>> ' 
    BORDER_LENGTH = 100
    VOWELS = ('A', 'E', 'U', 'I', 'O')
    CONSONANTS = ('Q', 'W', 'R', 'T', 'Y', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M')
    # Initialise needed attributes
    def __init__(self):
        
        self.__phraseForRound = {'category': '', 'phrase': []}
        self.__phraseAsBlankChars = []
        # ['■' * len(word) for word in self.__phraseForRound['phrase']]
        self.__vowelsInPhrase = []
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
        print('=' * self.BORDER_LENGTH)
        print('Wheel of Fortune'.center(self.BORDER_LENGTH))
        print('=' * self.BORDER_LENGTH)
    
    # Method used to get names of players
    def getPlayerNames(self):
        print('Please enter the names for the players playing')
        for i in range(3):
            self.__scores[i]['user'] = input(f'Player {i + 1} name\n{self.INPUT_FIELD}')
        print('Okay contestants, let\'s play our first round')
    
    # Method used to get length of phrases file, this is done to allow users to add more phrases to the file (if they want to) 
    # and have program not crash
    def getLengthOfPhraseFile(self):
        with open('phrases.txt', 'r') as phrasesFile:
            # List comprehension, we go over each line in the file and get a value of 1, to get the 
            # number of lines in the file
            self.__numberOfLines = sum([1 for line in phrasesFile])
                    
    # Method used to get a random phrase from the phrases file
    def getPhraseForRound(self):
        # Get a random integer, this will be the random line in the file
        randomLine = random.randint(1, self.__numberOfLines)
        
        # Variable to store phrase 
        phrase = ''
        # Read the file 
        with open('phrases.txt', 'r') as phrasesFile:
            for i in range(randomLine):
                phrase = phrasesFile.readline()
            # Once phrase found, split it to category and phrase
            phrase = phrase.rstrip('\n').split('-')
            print(phrase)

        # Save to the appropriate attributes
        self.__phraseForRound['category'] = phrase[0]
        self.__phraseForRound['phrase'] = phrase[1].upper()

        # Make a version of the phrase as blank characters to show to players during the game    
        # Each word becomes a row of equal signs 
        self.__phraseAsBlankChars = ['=' * len(word) for word in self.__phraseForRound['phrase'].split()]

        # This is used to keep track of vowels in the phrase. 
        # Used to check when players bought every vowel
        # First we loop through the vowels in the VOWELS constant tuple
        for vowel in self.VOWELS:
            # If the word contains the vowel, we append the vowel to the __vowelsInPhrase attribute
            if vowel in self.__phraseForRound['phrase']:
                self.__vowelsInPhrase.append(vowel)
        # print(self.__vowelsInPhrase)

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
        self.__wheelValues = random.choices(range(100, 1500, 100), k = 10)

    # Method used to spin the wheel, takes a list of values
    def spinWheel(self, values):
        # From the passes list, we randomly choose one
        landedValue = random.choice(values)

        # Characters for animation for spinning wheel
        spinWheelChars = ['|', '/', '-', '\\', '|', '/', '-', '\\']

        # This loop is used to show the animation of a wheel spinning
        for i in range (2):
            for k in range (len(spinWheelChars)):
                # Pause execution to allow user to see characters changing
                time.sleep(.1)
                print('Spinning wheel', spinWheelChars[k], end='\r')
        print()
        # Return the value that the wheel landed on
        return landedValue

    # Method used to play a round of wheel of fortune 
    def playRound(self):
        # Print a introductory message
        print(f'The category for this round is: {self.__phraseForRound['category']}')

        # Generate the values for the wheel
        self.generateValuesForWheel()
        self.printListInLine(self.__wheelValues, 'The values on the wheel are')

        # List used to store the money earned in the round
        scoresCurrentRound = [
            {'user': self.__scores[0]['user'], 'money': 0},
            {'user': self.__scores[1]['user'], 'money': 0},
            {'user': self.__scores[2]['user'], 'money': 0},
        ]

        # Sentinel variable used to keep round going till the phrase is solved
        phraseSolved = False
        # Loop to play game, each player takes turn to spin wheel and guess the letters of the phrase
        while not phraseSolved:
            # Create sets to store consonant and vowels guessed/purchased
            guessedConsonants = set()
            purchasedVowels = set()
            self.__vowelsRevealed = False
            # Loop through __scores object, to let each player play
            for i in range(len(scoresCurrentRound)):
                # Sentinel variable used to keep track if a player's turn is over
                # It ends when they guess a consonant, vowel or the phrase wrong
                turnOver = False
                while not turnOver:
                    # At start of each turn print the money each player has
                    self.displayScores(scoresCurrentRound, 'Current Scores:')
                    # Show the current phrase as blank characters, to user
                    # This gets filled in with letters as the players guess the letters
                    print('\nHere is your phrase')
                    print(' '.join(self.__phraseAsBlankChars))
                    
                    # Show the guessed consonants and bought vowels
                    self.printListInLine(guessedConsonants, 'Guessed Consonants')
                    self.printListInLine(purchasedVowels, 'Purchased Vowels')
                    
                    # Let user spin the wheel
                    print(f'\n{scoresCurrentRound[i]['user']} it is your turn, press enter to spin the wheel!')
                    input(self.INPUT_FIELD)
                    landedValue = self.spinWheel(self.__wheelValues)
                    print(f'\nYou landed on ${landedValue}\n')

                    # Ask user on what they would like to do
                    # If all the vowels have been revealed, we remove the vowel option
                    if self.__vowelsRevealed == False:
                        userInput = self.handleMenuSelection(['Guess consonant', 'Solve the phrase', 'Buy a vowel'])
                    else:
                        userInput = self.handleMenuSelection(['Guess consonant', 'Solve the phrase'])

                    # Call the appropriate method based on user input
                    # The turnOver variable will gets a new boolean value to determine if the players
                    # turn is over or not
                    if userInput == 1:
                        turnOver = self.playerGuessesConsonant(landedValue, guessedConsonants, i, scoresCurrentRound)
                    elif userInput == 2:
                        # If solved we set the sentinel variables to their appropriate values to exit the loop
                        # and store which player solved the puzzle
                        turnOver, phraseSolved, player = self.playerSolvePhrase(i)
                    elif userInput == 3:
                        turnOver = self.playerBuysVowel(landedValue, purchasedVowels, guessedConsonants, i, scoresCurrentRound)
                
                # When phrase is solved, we break out of the game loop        
                if phraseSolved: 
                    break
        # After puzzle solved inform players and add the money earned for the player that solved the puzzle
        print('Round over')
        print(f'Great job {scoresCurrentRound[player]['user']}! The money earned from this round will be added to your total.')
        self.__scores[player]['money'] += scoresCurrentRound[player]['money']
        self.displayScores(self.__scores, 'Scores after the puzzle:')
        time.sleep(2)

        
                       

    # Method used to handle user wanting to guess a consonant in the phrase
    def playerGuessesConsonant(self, landedValue, guessedConsonants, player, scores):
        # Print the phrase and the guesses consonants
        print(f'\nPhrase:\n{' '.join(self.__phraseAsBlankChars)}')
        self.printListInLine(guessedConsonants, 'Guessed Consonants')
        
        # Ask user to enter a consonant
        validInput = False
        while not validInput:
            userInput = input(f'\nGuess a consonant in the phrase\n{self.INPUT_FIELD}').upper().rstrip()
            # Check to see if user entered nothing, if not they are prompted to enter a letter again
            if userInput in self.VOWELS or userInput ==' ' or userInput == '':
                validInput = False
                print('Please enter a consonant\n')
                continue
            validInput = True
        else:
            # We need to check that they entered a character that, if it is their turn ends
            if userInput in guessedConsonants:
                print(f'\nSorry, "{userInput}" was already guessed, you turn has ended.')
                
                time.sleep(1)
                return True

        # Keep track of constants guessed
        guessedConsonants.add(userInput)

        # Check to see how many instances of the user entered consonant is in the phrase
        num = self.checkForCharInPhrase(self.__phraseForRound['phrase'], userInput)
        
        # Based on the number of instances of the consonant, print an appropriate message
        # If the consonant is in the phrase, we need to update the list that stores the phrase
        # with blank characters
        if num > 1:
            print(f'\nThere are {num} {userInput}s!')
            self.replaceBlankStrWithChars(userInput)
        elif num == 1:
            print(f'\nThere is 1 {userInput}')
            self.replaceBlankStrWithChars(userInput)
        else:
            # When player does not get any characters correct, their turn ends
            print(f'\nSorry there are no "{userInput}" in the phrase. Next players turn.')
            time.sleep(1)
            return True
            
        # Add user score
        # This depends on the number of instance of the letter times the number the user landed on with the wheel
        print(f'Money earned: {num * landedValue}')
        scores[player]['money'] += num * landedValue
        time.sleep(1)
        # Return false to allow user to spin again since they guesses correctly
        return False

    # Method used to allow user to purchase a vowel
    def playerBuysVowel(self, landedValue, purchasedVowels, guessedConsonants, player, scores):
        # Cost of a vowel
        VOWEL_COST = 250

        # Sentinel variable to allow user purchase another vowel
        # Loop till user does not want to buy another vowel, or they cannot buy another one
        buyAnother = 'Y'
        while buyAnother == 'Y':
            # Print user their balance and the cost of a vowel
            print(f'\nYour balance: {scores[player]['money']}\t\t Cost of vowel: {VOWEL_COST}')
            # First check if user has enough money to buy a vowel
            if scores[player]['money'] <= VOWEL_COST:
                print('Sorry, you don\'t have enough money to buy a vowel')
                time.sleep(1)
                break # stop the loop

            # Print the phrase with blank characters and the purchases vowels
            print(f'\nPhrase:\n{' '.join(self.__phraseAsBlankChars)}')
            self.printListInLine(purchasedVowels, 'Purchased Vowels')

            # Ask user to enter a vowel
            validInput = False
            # Loop till user enters a valid input
            while not validInput:
                userInput = input(f'\nWhich vowel would you like to buy?\n{self.INPUT_FIELD}').upper().rstrip()
                # Check if user entered nothing or if they entered a consonant
                # If so the user needs to enter a vowel to continue
                if userInput in self.CONSONANTS or userInput == ' ' or userInput == '':
                    validInput = False
                    print('Please buy a vowel!\n')
                    continue
                # If input valid, set sentinel variable to true
                validInput = True
            else:
                # After player enters a vowel, we check to see if the vowel was bought already 
                # If it was, their turn is over
                if userInput in purchasedVowels:
                    print(f'\nSorry, "{userInput}" was already purchases, you turn has ended.')
                    time.sleep(1)
                    return True
            

            # Keep track of vowels purchases
            purchasedVowels.add(userInput)

            # Subtract cost of vowel to player's balance
            scores[player]['money'] -= VOWEL_COST 

            # Check to see how many of the purchased vowel are in the phrase
            num = self.checkForCharInPhrase(self.__phraseForRound['phrase'], userInput)
            
            # Display appropriate message based on number of vowels in the phrase
            if num == 0:
                print(f'Sorry there is no "{userInput}" in the phrase. Your turn ends')
                time.sleep(1)
                # Exit the function, when player buys a vowel not in the phrase, their turn ends
                return True
            elif num > 1: 
                print(f'\nThere are {num} "{userInput}" in the phrase')
                self.replaceBlankStrWithChars(userInput)
                print(f'\nPhrase:\n{' '.join(self.__phraseAsBlankChars)}')
                time.sleep(1)
            else: 
                print(f'\nThere is 1 "{userInput}" in the phrase')
                self.replaceBlankStrWithChars(userInput)
                print(f'\nPhrase:\n{' '.join(self.__phraseAsBlankChars)}')
                time.sleep(1)

            # We remove the vowel from this list to keep track of vowels not revealed yet
            self.__vowelsInPhrase.remove(userInput)
            print(self.__vowelsInPhrase)
            # Once all the vowels have been bought, we inform players of it
            if len(self.__vowelsInPhrase) == 0:
                print('No more vowels left to buy!\n')
                self.__vowelsRevealed = True
                time.sleep(1)
                break

            # Ask user if they would like to buy another vowel
            print(f'\nYour balance: {scores[player]['money']}')
            buyAnother = input(f'\nWould you like to buy another vowel? (Y?)\n{self.INPUT_FIELD}').upper()
            print()

        # Once user does not want to buy another vowel or no more vowels available to buy, they can either guess a consonant or the phrase
        # Ensure input is valid
        userInput = self.handleMenuSelection(['Guess a consonant', 'Solve the phrase'])
        if userInput == 1:
            return self.playerGuessesConsonant(landedValue, guessedConsonants, player, scores)
        elif userInput == 2:
            pass
    
    # Method used to handle players solving the phrase
    def playerSolvePhrase(self, player):
        # Show the partially solved phrase and prompt user for guess
        print(f'\nPhrase:\n{' '.join(self.__phraseAsBlankChars)}')
        print('\nType the puzzle word for word')
        userInput = input(self.INPUT_FIELD).rstrip().upper()

        if userInput == self.__phraseForRound['phrase']:
            # If guess correct, inform players, return boolean values to exit loop and player who solved it 
            print(f'Correct! the phrase was: {self.__phraseForRound['phrase']}')
            time.sleep(1)
            return True, True, player
        else:
            # If guess incorrect, current players turn is over
            print('Wrong, next players turn!')
            time.sleep(1)
            return True, False, None
            
    # Method used to check if a character entered by the player is in the phrase
    # It returns an int of how many instances of the character is in the phrase
    def checkForCharInPhrase(self, phrase, char):
        num = 0
        for word in phrase:
            num += word.count(char)
        return num
        
    # Method used to replace blank characters in phrase to correct guessed/purchases characters
    def replaceBlankStrWithChars(self, userInput):
        # Variable used to keep track of the words index in the __phraseAsBlankChars list
        wordIndex = 0
    
        # Loop through each word in the phrase for the round
        for word in self.__phraseForRound['phrase'].split():
            # Variable used to keep track of the current characters index
            charIndex = 0
            # Loop through every character in the word
            for char in word:                
                
                # If the character equals the character the user entered, we replace the blank character in __phraseAsBlankChars
                # with the appropriate letter
                if char == userInput:    
                    # In order to replace the character, we slice the string. 
                    # First we slice the string from the start to the character before the one that needs to be replaced
                    # Then we concatenate the letter the user entered to the first slice
                    # Then slice the original string to get the rest of the string and concatenate it to the previous strings
                    self.__phraseAsBlankChars[wordIndex] = self.__phraseAsBlankChars[wordIndex][:charIndex] + userInput + self.__phraseAsBlankChars[wordIndex][charIndex + 1:]
                
                # Increment the variable
                charIndex += 1
            wordIndex += 1

    # Method used to print a list/set in a row
    def printListInLine(self, list, title):
            print(f'\n{title}:')
            for word in list:
                print(f'{word}\t', end = '')
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
        