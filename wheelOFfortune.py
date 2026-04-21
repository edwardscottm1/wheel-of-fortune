'''This file will contain the class used to play the wheel of fortune game'''


import random

class wheelOfFortuneGame:
    INPUT_FIELD = '>> ' 
    BORDER_LENGTH = 100
    # Initialise needed attributes
    def __init__(self):
        
        self.__phrase = {}
        self.__scores = [ 
            {'user':'', 'money': 0},
            {'user':'', 'money': 0},
            {'user':'', 'money': 0}
        ]

    def printGameRules(self):
        print('=' * self.BORDER_LENGTH)
        print('Wheel of Fortune'.center(self.BORDER_LENGTH))
        print('=' * self.BORDER_LENGTH)
    
    def getPlayerNames(self):
        print('Please enter the names for the players playing')
        for i in range(3):
            self.__scores[i]['user'] = input(f'Player {i + 1} name\n{self.INPUT_FIELD}')
        print('Okay contestants, let\'s play our first round')

    def getPhraseForRound(self):
        with open('phrases.txt', 'r') as phrasesFile:
            phrase = phrasesFile.readline().rstrip('\n').split('-')
            print(phrase)

