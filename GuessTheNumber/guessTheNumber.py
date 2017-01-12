import random;
theNumber = random.randint(0,20)
#print('the number: ', theNumber)


theGuess = 21 # they have to be wrong the first guess to start the loop
guesses = 5


while theGuess != theNumber:
    print('take a guess between (1-20): [left: ' + str(guesses) + ']')
    theGuess = int(input())

    if theGuess == theNumber:
        print('You Win!')
    elif theGuess <= theNumber+2 and theGuess >= theNumber-2:
        print('Hot')
    elif theGuess <= theNumber+5 and theGuess >= theNumber-5:
        print('warm')
    elif theGuess <= theNumber+7 and theGuess >= theNumber-7:
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
