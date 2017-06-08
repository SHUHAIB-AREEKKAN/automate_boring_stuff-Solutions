theBoard={'top-L':'O','top-M':'O','top-R':'O',
	 'mid-L':'X','mid-M':'X','mid-R':'',
	 'low-L':'','low-M':'','low-R':'X'}

def printBoard(board):
	print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
	print('-+-+-')
	print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
	print('-+-+-')
	print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
turn='X'
for i in range(9):
	printBoard(theBoard)
	print('turn for '+turn+'on which place?')
	move=input()
	theBoard[move]=turn
	if turn=='X':
		trun='O'
	else:
		turn='X'

printBoard(theBoard)



	
