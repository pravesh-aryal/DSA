def isValidSudoku(board):

	rowHashSet = set()
	colHashSet = set()
	i, j = 0, 0
	matrixHashSet = set()
	

	while i < 9:
		j = 0
		while j < 9:

			if (i % 3 == 0 and j % 3 == 0):
				#add 3 by 3 sub-matrix to the matrixHashSet
				for a in range(0, 3):
					for b in range(0, 3):
						if board[i+a][j+b] in matrixHashSet:
							return False
						if board[i+a][j+b] != ".":
							matrixHashSet.add(board[i+a][j+b])
				matrixHashSet = set()
			if board[i][j] in rowHashSet:
				return False
			if board[j][i] in colHashSet:
				return False
			if board[i][j] != "." and board[j][i] != ".":
				rowHashSet.add(board[i][j])
				colHashSet.add(board[j][i])
				
			j += 1
			

		rowHashSet = set()
		colHashSet = set()

		i += 1

	return True #if all goes well

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))


			

        
"""
(0,0) (0, 3) (0,6)
(3,0) (3, 3) (3,6)
(6,0) (6,3). (6,6)

for 
0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2
  
"""