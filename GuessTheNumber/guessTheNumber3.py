import random;
theNumber = random.randint(0,20)
#print('the number: ', theNumber)


theGuess = 21 # they have to be wrong the first guess to start the loop
guesses = 5

# Set temp ranges
def isInRange(guess, temp):
    return guess <= theNumber+temp and guess >= theNumber-temp


while theGuess != theNumber:
    print('take a guess between (1-20): [left: ' + str(guesses) + ']')
    theGuess = int(input())

    if theGuess == theNumber:
        print('You Win!')
    elif isInRange(theGuess, 2):
        print('Hot')
    elif isInRange(theGuess, 5):
        print('warm')
    elif isInRange(theGuess, 7):
        print('cold')
    else:
        print('frozen')
    
#    if theGuess == theNumber:
#        print('You Win!')
#    elif theGuess < theNumber:
#        print('too low')
#    elif theGuess > theNumber:
#        print('Way too high person')
#    else:
#        print('You lose')
#        print('try again')

    guesses = guesses - 1
        


print('end')
