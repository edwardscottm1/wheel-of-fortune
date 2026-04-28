Wheel of Fortune Game by: Edward Scott

This is a simple reproduction of the game show Wheel of Fortune. To run this app, run the main.py file, in your console you'll 
be shown instructions on how to play and then you'll enter the names of the players playing. Afterwards, you'll play 3 rounds
where the goal is to solve the puzzle. Here are the rules:

    1. A puzzle and category will be revealed to users, the puzzle will be a bunch of blank characters, as users guess the letters
    the puzzle will be revealed. The round ends once a user solves the puzzle. 

    2. Each player will have a grand total and sub total during the round, 
       -- The total during the round is the money earned by guessing correct consonants. The user keeps this total 
          if they solve the puzzle correct, then it will be added to their grand total 
       -- After 3 rounds of play, the grand total is used to determine the winner
    
    3. Each player will take turns spinning the wheel during the round,        
        -- Land on BANKRUPT, the player loses the money earned from the round and their turn ends
        -- Land on LOSE TURN, the player turn's end and the next player gets to spin the wheel
        -- Land on money, the player then can guess a consonant, buy a vowel, or solve the puzzle. This value is used to determine 
           how much money they can earn
    
    4. When a player guesses a consonant,
        -- The player will be prompted to enter a consonant they think is in the puzzle 
        -- If the consonant is in puzzle, the consonant will be revealed in the puzzle, and the number of instance of 
           the consonant in the puzzle times the landed value will equal how much money the user earns for that guess. 
           The user then can spin the wheel again
        -- If the consonant is not in the puzzle, the player will lose their turn
        -- If the users guesses a consonant that was already guessed, the player will lose their turn
    
    5. When a user buys a vowel,
        -- The user will be prompted to enter a vowel they wish to buy
        -- Each vowel cost $250, each time a player buys a vowel $250 will be subtracted from their total in the current round
        -- If the vowel is not in puzzle, if the vowel is not in the puzzle, the player's turn ends
        -- If the vowel is in the puzzle, the vowel will be shown in the puzzle, the player can buy another vowel if they wish,
           after buying vowels the player can either guess a consonant or solve the puzzle

    6. When user wants to solve the puzzle,
        -- The player will be prompted to enter the puzzle correctly
        -- If entered correctly, the round ends and the money earned by the player that solves the puzzle will be added to their
           grand total.
        -- If entered incorrectly, the player loses their turn and the next player spins the wheel
    
    7. After 3 rounds of play a winner is determined,
        -- The player with the most amount of money earned will be the winner
        -- In the rare instance of a tie, the tied players will play rock paper scissors to determine the winner


For the best experience I recommend playing this game with a total of 3 players. It is possible to play the game by yourself but 
then you'll be playing as 3 different people at the same time.

You can find the puzzles.txt file in this folder, this contains puzzles that are used for each round in Wheel of Fortune. You may add your
own puzzles if you wish. Just ensure you enter the category of the puzzle then the puzzle on the same line separated by a dash (-). Remove any
lines that do not contain text.

Entries in puzzles.txt:   Family-Adopted Children Are Chosen Children
                          Family-Grandma Olive Oil
                          Family-The Wright Brothers 


Notes of the program:

Wheel of Fortune experts may notice that this reproduction does not have toss up rounds or the bonus round. The goal of this project was to
reproduce a typical round of Wheel of Fortune. I'm proud of the final result for this project. I felt that I did a good reproduction of the
game loop of Wheel Of Fortune. I struggled to figure out how to find a specific character in a string but I discovered various methods that
can be used to identify substrings within strings via w3schools. Also I learnt that strings are iterable just like lists/tuples/sets/
dictionaries. As I was working on the project I noticed it was hard at times to follow along what was happening in the console because
various print statements would scroll the window making you lose your place. I learn that the time module contain the sleep function
that can pause the program for a couple of seconds. I used these to allow users to easily follow along. In addition, I used this
function to create the spin wheel animation. I used the carriage return character and the sleep function to show a value on a wheel
for half a second then write over the line to show the next value till the wheel stopped "spinning."

I wish that I could have done this project with someone else. Many times as I was working on the project I was thinking how I could split the 
work so I can use one method with higher detail. Even though I didn't work with anyone, I challenged myself to learn a new tools that could
help developing and sharing future projects. I learn how to use Git and Github. I created my own repository with this project and each time
I made a change to the code I would commit and push it to the repo. Learning these tools showed me how I could use them in a pair programming
environment, where I would update the code and push it to the repo so others can work on it/improve upon it. I feel that now I have a 
good baseline understanding of how to implement Git/version control for future project. 

Here is a link to that repo: https://github.com/edwardscottm1/wheel-of-fortune