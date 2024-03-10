import random

# initialize variables
endProgram = "no"
playerOne = "NO NAME"
playerTwo = "NO NAME"

# call to inputNames
playerOne, playerTwo = inputNames(playerOne, playerTwo)

# while loop to run program again
while endProgram == 'no':

    # initialize variables
    p1number = 0
    p2number = 0
    winnerName = 'NO NAME'

    # call to rollDice
    winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)

    # call to displayInfo
    displayInfo(winnerName)

    # end of while loop
    endProgram = raw_input('Do you want to end program? (Enter yes or no): ')

# this function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne = input('Enter player 1 name: ')
    playerTwo = input('Enter player 2 name: ')
    return playerOne, playerTwo

# this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    if p1number == p2number:
        winnerName = "TIE"
    elif p1number > p2number:
        winnerName = playerOne
    else:
        winnerName = playerTwo
    return winnerName

# this function displays the winner
def displayInfo(winnerName):
    print('The winner is', winnerName)


# calls main
main()
