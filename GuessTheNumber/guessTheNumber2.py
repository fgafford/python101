import random;
theNumber = random.randint(0,20)
#print('the number: ', theNumber)


theGuess = 21 # they have to be wrong the first guess to start the loop
guesses = 5

# Set temp ranges
hLow = theNumber-2
hHigh = theNumber+2
wLow = theNumber-5
wHigh = theNumber+5
cLow = theNumber-7
cHigh = theNumber+7


while theGuess != theNumber:
    print('take a guess between (1-20): [left: ' + str(guesses) + ']')
    theGuess = int(input())

    if theGuess == theNumber:
        print('You Win!')
    elif theGuess <= hHigh and theGuess >= hLow:
        print('Hot')
    elif theGuess <= wHigh and theGuess >= wLow-5:
        print('warm')
    elif theGuess <= cHigh and theGuess >= cLow:
        print('cold')
    else:
        print('frozen')


    guesses = guesses - 1
        


print('end')
