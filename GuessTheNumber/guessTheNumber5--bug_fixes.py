# The user wants to play when the program starts.... (duh!)
play = True

# Loop as long as the player wants to play
while play:

    import random;
    theNumber = random.randint(0,20)
    #print('the number: ', theNumber)


    theGuess = -10000 # they have to be wrong the first guess to start the loop
    guesses = 5

    # Set temp ranges
    hot = 2
    warm = 5
    cold = 7

    # isInRange
    #
    # Tells you if the 'guess' is within the 'temp' range
    #
    # isInRange(int, int) -> Boolean
    def isInRange(guess, temp):
        return guess <= theNumber+temp and guess >= theNumber-temp


    while theGuess != theNumber:
        try:
            print('take a guess between (1-20): [left: ' + str(guesses) + ']')
            theGuess = int(input())
        except:
           print('I need a REAL number, YO!')
           continue


        if theGuess == theNumber:
            print('You Win!')
            print('Do you want to play again?(y/n)')
            again = input()
            if again == 'y':
                play = True
                break
            else:
                play = False

        elif isInRange(theGuess, hot):
            print('Hot')
        elif isInRange(theGuess, warm):
            print('warm')
        elif isInRange(theGuess, cold):
            print('cold')
        else:
            print('frozen')

        print('try again')
        guesses = guesses - 1

    print('end')
