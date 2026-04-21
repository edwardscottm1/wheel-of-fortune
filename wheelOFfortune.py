'''This file will contain the class used to play the wheel of fortune game'''


import random

class wheelOfFortuneGame:
    INPUT_FIELD = '>> ' 
    BORDER_LENGTH = 100
    # Initialise needed attributes
    def __init__(self):
        
        self.__phraseForRound = {'category': '', 'phrase': ''}
        self.__scores = [ 
            {'user':'', 'money': 0},
            {'user':'', 'money': 0},
            {'user':'', 'money': 0}
        ]
        self.__numberOfLines = 0

    def printGameRules(self):
        print('=' * self.BORDER_LENGTH)
        print('Wheel of Fortune'.center(self.BORDER_LENGTH))
        print('=' * self.BORDER_LENGTH)
    
    def getPlayerNames(self):
        print('Please enter the names for the players playing')
        for i in range(3):
            self.__scores[i]['user'] = input(f'Player {i + 1} name\n{self.INPUT_FIELD}')
        print('Okay contestants, let\'s play our first round')
    
    def getLengthOfPhraseFile(self):
        with open('phrases.txt', 'r') as phrasesFile:
            # List comprehension, we go over each line in the file and get a value of 1, to get the 
            # number of lines in the file
            self.__numberOfLines = sum([1 for line in phrasesFile])
                    

    def getPhraseForRound(self):
        randomLine = random.randint(1, self.__numberOfLines)
        # print(randomNum)
        phrase=''
        with open('phrases.txt', 'r') as phrasesFile:
            for i in range(randomLine):
                phrase = phrasesFile.readline()
            phrase = phrase.rstrip('\n').split('-')

        
        self.__phraseForRound['category'] = phrase[0]
        self.__phraseForRound['phrase'] = phrase[1]

        print(self.__phraseForRound)

