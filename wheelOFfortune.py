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
        self.__phraseAsBlankChars = ['■' * len(word) for word in self.__phraseForRound['phrase']]
        self.__vowelsInPhrase = []
        self.__scores = [ # placeholder values THIS NEED TO BE SET TO NOTHING WHEN DONE
            {'user':'Edward', 'money': 1000},
            {'user':'Elliott', 'money': 0},
            {'user':'Alex', 'money': 0}
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
            print(phrase)

        # Save to the appropriate attributes
        self.__phraseForRound['category'] = phrase[0]
        self.__phraseForRound['phrase'] = phrase[1].upper()

        # Make a version of the phrase as blank chars to show to players during the game     
        self.__phraseAsBlankChars = ['=' * len(word) for word in self.__phraseForRound['phrase'].split()]

        # This is used to keep track of vowels in the phrase. This is used to keep track of when players bought every vowel
        for vowel in self.VOWELS:
            # print(self.__phraseForRound['phrase'])
            if vowel in self.__phraseForRound['phrase']:
                self.__vowelsInPhrase.append(vowel)
        print(self.__vowelsInPhrase)

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
            guessedConsonants = set()
            purchasedVowels = set()
            for i in range(len(self.__scores)):
                turnOver = False
                while not turnOver:
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
                        turnOver = self.playerGuessesConsonant(landedValue, guessedConsonants, player = i)
                    elif userInput == 2:
                        turnOver = self.playerBuysVowel(landedValue, purchasedVowels, guessedConsonants, player = i)
                       


    def playerGuessesConsonant(self, landedValue, guessedConsonants, player):
        print(f'Phrase:\n{' '.join(self.__phraseAsBlankChars)}')
        self.printListInLine(guessedConsonants, 'Guessed Consonants')
        validInput = False
        while not validInput:
            userInput = input(f'\nGuess a consonant in the phrase\n{self.INPUT_FIELD}').upper()
            if userInput in self.VOWELS or userInput ==' ' or userInput == '':
                validInput = False
                print('Please enter a consonant\n')
                continue
            validInput = True
        else:
            if userInput in guessedConsonants:
                print(f'\nSorry, "{userInput}" was already guessed, you turn has ended.')
                
                time.sleep(1)
                return True

        # keep track of constants guessed
        guessedConsonants.add(userInput)

        # Check to see how many consonants in the phrase
        num = self.checkForCharInPhrase(self.__phraseForRound['phrase'], userInput)
        
            
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
            
        # Add score
        print(f'Money earned: {num * landedValue}')
        self.__scores[player]['money'] += num * landedValue
        time.sleep(1)
        return False

# what happens if user buys a vowel that is not in the word
# cost of vowel
# keep track of vowels
# can user guess a consonant if they bought a vowel

    def playerBuysVowel(self, landedValue, purchasedVowels, guessedConsonants, player):
        VOWEL_COST = 250
        

        buyAnother = 'Y'

        while buyAnother == 'Y':
            print(f'Your balance: {self.__scores[player]['money']}\t\t Cost of vowel: {VOWEL_COST}')
            if self.__scores[player]['money'] < VOWEL_COST:
                print('Sorry, you don\'t have enough money to buy a vowel')
                time.sleep(1)
                break

            print(f'\nPhrase:\n{' '.join(self.__phraseAsBlankChars)}')
            self.printListInLine(purchasedVowels, 'Purchased Vowels')

            validInput = False
            userInput = ''
            while not validInput:
                userInput = input(f'\nWhich vowel would you like to buy?\n{self.INPUT_FIELD}').upper()
                if userInput in self.CONSONANTS or userInput == ' ' or userInput == '':
                    validInput = False
                    print('Please buy a vowel!\n')
                    continue
                validInput = True
            else:
                if userInput in purchasedVowels:
                    print(f'\nSorry, "{userInput}" was already purchases, you turn has ended.')
                    time.sleep(1)
                    return True
            


            purchasedVowels.add(userInput)
            self.__scores[player]['money'] -= VOWEL_COST 
            # Check to see how many of the purchased vowel are in the phrase
            num = self.checkForCharInPhrase(self.__phraseForRound['phrase'], userInput)
            
            
            if num == 0:
                print(f'Sorry there is no "{userInput}" in the phrase. Your turn ends')
                time.sleep(1)
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

            # Once all the vowels have been bought, we inform players of it
            self.__vowelsInPhrase.remove(userInput)
            print(self.__vowelsInPhrase)
            if len(self.__vowelsInPhrase) == 0:
                print('No more vowels left to buy!\n')
                time.sleep(1)
                break


            print(f'\nYour balance: {self.__scores[player]['money']}')
            buyAnother = input(f'\nWould you like to buy another vowel? (Y?)\n{self.INPUT_FIELD}').upper()
            print()

        # Ensure input is valid
        inputValid = False
        while not inputValid:
            try:
                print('Choose from the options below:\n1. Guess a consonant\n2. Guess the phrase\n')
                userInput = int(input(self.INPUT_FIELD))
                if userInput > 0 and userInput < 2:
                    inputValid = True
                else:
                    print('\nPlease enter a valid option')
            except ValueError:
                print('\nPlease enter a valid option')
        print()
        if userInput == 1:

            return self.playerGuessesConsonant(landedValue, guessedConsonants, player)
        



            

            
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
    
    def checkForCharInPhrase(self, phrase, char):
        num = 0
        for word in phrase:
            num += word.count(char)
        return num
        
    def replaceBlankStrWithChars(self, userInput):
        index = 0
        for word in self.__phraseForRound['phrase'].split():
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
    def handleMenuSelection(self, options):
        pass