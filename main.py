import wheelOFfortune



NUM_OF_ROUNDS = 3

def main():
    WheelOfFortune = wheelOFfortune.wheelOfFortuneGame()
    WheelOfFortune.printGameRules()
    WheelOfFortune.getPlayerNames()
    WheelOfFortune.getLengthOfPuzzleFile()
    for i in range(NUM_OF_ROUNDS):
        WheelOfFortune.getPuzzleForRound()
        WheelOfFortune.playRound()
        if i < NUM_OF_ROUNDS - 1:
            print('\n\nLet\'s play our next round!\n\n')
    WheelOfFortune.determineWinner()
    WheelOfFortune.farewell()

if __name__ == '__main__':
    main()