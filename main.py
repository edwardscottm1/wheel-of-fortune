import wheelOFfortune



NUM_OF_ROUNDS = 3

def main():
    WheelOFfortune = wheelOFfortune.wheelOfFortuneGame()
    # WheelOFfortune.printGameRules()
    # WheelOFfortune.getPlayerNames()
    WheelOFfortune.getLengthOfPhraseFile()
    for i in range(NUM_OF_ROUNDS):
        WheelOFfortune.getPhraseForRound()
        WheelOFfortune.playRound()
        if i < NUM_OF_ROUNDS - 1:
            print('\nLet\'s play our next round!\n\n')

if __name__ == '__main__':
    main()