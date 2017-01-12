# A Game of Tic-Tac-Toe for 2 players....

# Variables we need to play the Game
# player 1
p1Name = 'player1'
p1Symbol = 'X'
# player 2
p2Name = 'player2'
p2Symbol = 'O'
# the board -- nested lists of Strings
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

# print the board to the console (screen)
# board -> None
def printBoard(board):
	print() # empty line

	print(board[0][0],'|',board[0][1],'|',board[0][2])
	print('----------')
	print(board[1][0],'|',board[1][1],'|',board[1][2])
	print('----------')
	# ERROR wrong row index
	print(board[2][0],'|',board[2][1],'|',board[2][2])

	print() # empty line

# Gets input from player about what move then want to do
# Sting (PlayerName)-> Int (Players move 1-9)
def getPlayerMove(pName):
	print(pName,'Make a move (Choose a number beteen 1-9):')
	# make sure to parse into an int
	return int(input())

# Place players symbol on the board when they reqested it
# String (players symbol), Int (location of the move) -> None
def playMove(pSymbol, location):
	# Row 1
	if(location == 1):
		board[0][0] = pSymbol
	elif(location == 2):
		board[0][1] = pSymbol
	elif(location == 3):
		board[0][2] = pSymbol
	# Row 2
	elif(location == 4):
		board[1][0] = pSymbol
	elif(location == 5):
		board[1][1] = pSymbol
	elif(location == 6):
		board[1][2] = pSymbol
	# Row 3
	elif(location == 7):
		board[2][0] = pSymbol
	elif(location == 8):
		board[2][1] = pSymbol
	elif(location == 9):
		board[2][2] = pSymbol


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
