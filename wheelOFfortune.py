'''This file will contain the class used to play the wheel of fortune game'''
# 3 hours

import random
import time

class wheelOfFortuneGame:
    INPUT_FIELD = '>> ' 
    BORDER_LENGTH = 100
    # Initialise needed attributes
    def __init__(self):
        
        self.__phraseForRound = {'category': '', 'phrase': []}
        self.__phraseAsBlankChars = []
        self.__scores = [ 
            {'user':'', 'money': 0},
            {'user':'', 'money': 0},
            {'user':'', 'money': 0}
        ]
        self.__numberOfLines = 0
        self.__wheelValues = []

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
        self.__phraseForRound['phrase'] = phrase[1].split()

        # Make a version of the phrase as blank chars to show to players during the game     
        self.__phraseAsBlankChars = ['■' * len(word) for word in self.__phraseForRound['phrase']]


    # Used to play logic of wheel of fortune game
    def playRound(self):
        print(f'The category for this round is: {self.__phraseForRound['category']}')
        print('Here is your phrase')
        print(' '.join(self.__phraseAsBlankChars))

        self.generateValuesForWheel()

        # Loop to play game, each player takes turn to spin wheel and guess the letters of the phrase
        for i in range(len(self.__scores)):
            #print(f'{self.__scores[i]['user']} it is your turn, press enter to spin the wheel!')
            input(self.INPUT_FIELD)
            landedValue = self.spinWheel(self.__wheelValues)
            print(f'You landed on ${landedValue}\n')

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
        