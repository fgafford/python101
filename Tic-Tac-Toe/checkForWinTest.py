'''
This is a Test Program

One very important thing you go do to make sure you program is going to work is
to test it. We could play every possible game of Tic-Tac-Toe to test and see if
it works. Or we could write another progam that tests out code for us. The 2nd
way is much faster.

This program tests the checkForWin function we use in our fame to see if it will
catch when a player wins or looses.
'''

'''
Here is were we place the function we want to test
if out checkForWin function calls any other function we will need to
include those functions here as well (like the match function)
'''

# This is the match function we wrote in calss
# we also forgot to check to make sure that the space is not empty
# if all three spaces are empty they still match so we have to check
# that as well as make sure that a == b and b == c
def match(a,b,c):
	return (a != ' ') and (a == b and b == c)

# Your check function here
def checkForWin(b):
	# WRITE YOUR FUNCTION HERE!!!

'''
This is the function that runs the actual test.
We give it a board and tell it if the test should pass.

The Vertical, Horizontal, and Diagonal tests should pass
The 'fail' test should fail (return false from our check function)
'''
def runTest(board, shouldBeTrue):
	result = checkForWin(board)
	if shouldBeTrue == result:
		print('Test passed!')
	else:
		print('Test Failed :(')
		print('Board was:')
		print(printBoard(board))

# print the board to the console (screen)
# board -> None
def printBoard(board):
	print() # empty line
	print(board[0],'|',board[1],'|',board[2])
	print('----------')
	print(board[3],'|',board[4],'|',board[5])
	print('----------')
	print(board[6],'|',board[7],'|',board[8])
	print() # empty line


'''
These are some test boards we will use these to test our check function
'''
# Some horizonal win boards
topH1 = ['O','O','O',' ',' ',' ',' ',' ',' ']
topH2 = ['X','X','X',' ',' ',' ',' ',' ',' ']
midH1 = [' ',' ',' ','O','O','O',' ',' ',' ']
midH2 = [' ',' ',' ','X','X','X',' ',' ',' ']
lowH1 = [' ',' ',' ',' ',' ',' ','O','O','O']
lowH2 = [' ',' ',' ',' ',' ',' ','X','X','X']
# Horizontal tests
runTest(topH1, True)
runTest(topH2, True)
runTest(midH1, True)
runTest(midH2, True)
runTest(lowH1, True)
runTest(lowH2, True)



# Some verital win boards
leftV1 = ['O',' ',' ','O',' ',' ','O',' ',' ']
leftV2 = ['X',' ',' ','X',' ',' ','X',' ',' ']
midV1 = [' ','O',' ',' ','O',' ',' ','O',' ']
midV2 = [' ','X',' ',' ','X',' ',' ','X',' ']
rightV1 = [' ',' ','O',' ',' ','O',' ',' ','O']
rightV2 = [' ',' ','X',' ',' ','X',' ',' ','X']
# Vertical tests
runTest(leftV1, True)
runTest(leftV2, True)
runTest(midV1, True)
runTest(midV2, True)
runTest(rightV1, True)
runTest(rightV2, True)



# Some diagonal win boards
diagonal1 = ['O',' ',' ',' ','O',' ',' ',' ','O']
diagonal2 = ['X',' ',' ',' ','X',' ',' ',' ','X']
diagonal3 = [' ',' ','O',' ','O',' ','O',' ',' ']
diagonal4 = [' ',' ','X',' ','X',' ','X',' ',' ']
# Diagonal Test
runTest(diagonal1, True)
runTest(diagonal2, True)
runTest(diagonal3, True)
runTest(diagonal4, True)


# Test that should fail.... no winner on board
fail1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
fail2 = ['O',' ','O',' ',' ','X',' ',' ','X']
fail3 = ['O','O','X','X','X','O','O','O','X']
# Tests that should NOT find a match
# Notice we pass in 'False' to the runTest function
runTest(fail1, False)
runTest(fail2, False)
runTest(fail3, False)
