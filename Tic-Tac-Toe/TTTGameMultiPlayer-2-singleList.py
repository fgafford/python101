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
	# 1. Complete this method!

# Place players symbol on the board
# pSymbol (String) : The players symbol
# location (int) : The index the user want to place their symbol at
#
# String (players symbol), Int (location of the move) -> None
def playMove(pSymbol, location):
	# 2. Complete this method!


# The actual game loop!
for c in range(9):
	# 3. Tell me what the next line does.
	if c%2 == 0:
		currentPName = p1Name
		currentPSymbol = p1Symbol
	else:
		currentPName = p2Name
		currentPSymbol = p2Symbol

	move = getPlayerMove(currentPName)
	playMove(currentPSymbol, move)
	printBoard(board)
