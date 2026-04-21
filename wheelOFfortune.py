'''This file will contain the class used to play the wheel of fortune game'''
# 3 hours

import random
import time

class wheelOfFortuneGame:
    INPUT_FIELD = '>> ' 
    BORDER_LENGTH = 100
    VOWELS = ['A', 'E', 'U', 'I', 'O']
    # Initialise needed attributes
    def __init__(self):
        
        self.__phraseForRound = {'category': 'test', 'phrase': ['THIS', 'IS', 'A', 'TEST']}
        self.__phraseAsBlankChars = []
        self.__phraseAsBlankChars = ['■' * len(word) for word in self.__phraseForRound['phrase']]
        self.__scores = [ # placeholder values THIS NEED TO BE SET TO NOTHING WHEN DONE
            {'user':'Edward', 'money': 2000},
            {'user':'Elliott', 'money': 3500},
            {'user':'Alex', 'money': 900}
        ]
        self.__numberOfLines = 0
        self.__wheelValues = []
        self.__turnOver = False

    # Print the game rules and title, NOT COMPLETE
    def printGameRules(self):
        print('=' * self.BORDER_LENGTH)
        print('Wheel of Fortune'.center(self.BORDER_LENGTH))
        print('=' * self.BORDER_LENGTH)
    
    # Get names of players
    def getPlayerNames(self):
        print('Please enter the names for the players playing')
        for i in range(3):
            self.__scores[i]['user'] = input(f'Player {i + 1} name\n{self.INPUT_FIELD}')
        print('Okay contestants, let\'s play our first round')
    
    # Get length of phrases file, this is done to allow users to add more phrases to the file 
    # and have program no crash
    def getLengthOfPhraseFile(self):
        with open('phrases.txt', 'r') as phrasesFile:
            # List comprehension, we go over each line in the file and get a value of 1, to get the 
            # number of lines in the file
            self.__numberOfLines = sum([1 for line in phrasesFile])
                    
    # Get a random phrase from the phrases file
    def getPhraseForRound(self):
        randomLine = random.randint(1, self.__numberOfLines)
        
        # Variable to store phrase 
        phrase = ''
        with open('phrases.txt', 'r') as phrasesFile:
            for i in range(randomLine):
                phrase = phrasesFile.readline()
            # Once phrase found, split it to category and phrase
            phrase = phrase.rstrip('\n').split('-')

        # Save to the appropriate attributes
        self.__phraseForRound['category'] = phrase[0]
        self.__phraseForRound['phrase'] = phrase[1].upper().split()

        # Make a version of the phrase as blank chars to show to players during the game     
        self.__phraseAsBlankChars = ['■' * len(word) for word in self.__phraseForRound['phrase']]

    def displayScores(self):
        print('\nCurrent Score')
        for i in range(len(self.__scores)):
            print(f'{self.__scores[i]['user']:^10}\t', end = '')
        print()
        for i in range(len(self.__scores)):
            print(f'${self.__scores[i]['money']:^10.2f}\t', end = '')
        print()

    # Used to play logic of wheel of fortune game
    def playRound(self):
        print(f'The category for this round is: {self.__phraseForRound['category']}')

        self.generateValuesForWheel()

        phraseGuessed = False
        # Loop to play game, each player takes turn to spin wheel and guess the letters of the phrase
        while not phraseGuessed:
            guessedConsonants = []
            purchasedVowels = []
            for i in range(len(self.__scores)):
                self.__turnOver = False
                while not self.__turnOver:
                    self.displayScores()

                    print('\nHere is your phrase')
                    print(' '.join(self.__phraseAsBlankChars))
                    
                    self.printListInLine(guessedConsonants, 'Guessed Consonants')
                    self.printListInLine(purchasedVowels, 'Purchased Vowels')
                    

                    print(f'\n{self.__scores[i]['user']} it is your turn, press enter to spin the wheel!')
                    input(self.INPUT_FIELD)
                    landedValue = self.spinWheel(self.__wheelValues)
                    print(f'\nYou landed on ${landedValue}\n')

                    # Ensure input is valid
                    inputValid = False
                    while not inputValid:
                        try:
                            print('Choose from the options below:')
                            print('1. Guess a consonant')
                            print('2. Buy a vowel')
                            print('3. Guess the phrase\n')
                            userInput = int(input(self.INPUT_FIELD))
                            if userInput > 0 and userInput < 4:
                                inputValid = True
                            else:
                                print('\nPlease enter a valid option')
                        except ValueError:
                            print('\nPlease enter a valid option')
                    print()

                    if userInput == 1:
                        self.playerGuessesConsonant(landedValue, guessedConsonants, player = i)
                       


    def playerGuessesConsonant(self, landedValue, guessedConsonants, player):
        print(f'Phrase:\n{' '.join(self.__phraseAsBlankChars)}')
        validInput = False
        while not validInput:
            userInput = input(f'Guess a consonant in the phrase\n{self.INPUT_FIELD}').upper()
            if userInput in self.VOWELS:
                validInput = False
                print('Do not enter a vowel!\n')
                continue
            validInput = True

        # keep track of constants guessed
        guessedConsonants.append(userInput)

        count = 0
        for word in self.__phraseForRound['phrase']:
            count += word.count(userInput)
            
        if count > 1:
            print(f'\nThere are {count} {userInput}s!')
            self.replaceBlankStrWithChars(userInput)
            time.sleep(1)
        elif count == 1:
            print(f'\nThere is 1 {userInput}')
            self.replaceBlankStrWithChars(userInput)
            time.sleep(1)
            
        else:
            # When player does not get any characters correct, their turn ends
            print(f'\nSorry there are no {userInput}s in the phrase. Next players turn.')
            self.__turnOver = True
            time.sleep(1)
            

        # Add score
        self.__scores[player]['money'] += count * landedValue

        

            
    # Generates values for the wheel
    def generateValuesForWheel(self):
        self.__wheelValues = random.choices(range(100, 1500, 100), k = 10)

    # Spin the wheel 
    def spinWheel(self, values):
        landedValue = random.choice(values)

        # Animation for spinning wheel
        spinWheelChars = ['|', '/', '-', '\\', '|', '/', '-', '\\']
        for i in range (2):
            for k in range (len(spinWheelChars)):
                time.sleep(.1)
                print('Spinning wheel', spinWheelChars[k], end='\r')
        print()
        return landedValue
        
    def replaceBlankStrWithChars(self, userInput):
        index = 0
        for word in self.__phraseForRound['phrase']:
            indexOfChar = -1
            for char in word:
                indexOfChar += 1
                if char == userInput:    
                    self.__phraseAsBlankChars[index] = self.__phraseAsBlankChars[index][:indexOfChar] + userInput + self.__phraseAsBlankChars[index][indexOfChar + 1:] 
            #print(self.__phraseAsBlankChars)
            index +=1

    def printListInLine(self, list, title):
            print(f'\n{title}:')
            for word in list:
                print(f'{word}\t', end = '')
            print()