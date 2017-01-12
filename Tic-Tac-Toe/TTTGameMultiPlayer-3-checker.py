# A Game of Tic-Tac-Toe for 2 players....

# Variables we need to play the Game
# player 1
p1Name = 'player1'
p1Symbol = 'X'
# player 2
p2Name = 'player2'
p2Symbol = 'O'
# the board -- list of Strings
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

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

# Gets input from player about what move then want to do
# pName (String) : Player's Name
#
# Sting (pName)-> Int (Players move 0-8)
def getPlayerMove(pName):
	print(pName,'Make a move (Choose a number beteen 1-9):')
	# make sure to parse into an int
	return int(input())

# Place players symbol on the board
# pSymbol (String) : The players symbol
# location (int) : The index the user want to place their symbol at
#
# String (players symbol), Int (location of the move) -> None
def playMove(pSymbol, location):
	board[location] = pSymbol

# Checks to see if all three of the passed in Strings are the same.
#
# String, String, String -> Boolean
def match(a,b,c):
	return (a != ' ') and (a == b and b == c)

def checkForWin(b):
			# Horizontal lines
	return (match(b[0],b[1],b[2]) or
			match(b[3],b[4],b[5]) or
			match(b[6],b[7],b[8]) or
			# Vertical lines
			match(b[0],b[3],b[6]) or
			match(b[1],b[4],b[7]) or
			match(b[2],b[5],b[8]) or
			# Diagonal lines
			match(b[0],b[4],b[8]) or
			match(b[2],b[4],b[6]))

# The actual game loop!
for c in range(9):
	if c%2 == 0:
		currentPName = p1Name
		currentPSymbol = p1Symbol
	else:
		currentPName = p2Name
		currentPSymbol = p2Symbol

	move = getPlayerMove(currentPName)
	playMove(currentPSymbol, move)
	printBoard(board)
	print('win:',checkForWin(board))
