def createBoard(N):
	# Board stores the squaremappings - ladder bottom->top, snake mouth->tail
	board = [i for i in range(0, N)]

	# Retrieve input from input.txt file
	with open("input.txt") as f:
	    inputFile = f.readlines()

	# Get ladders and update board[bottom_of_ladder] to top_of_ladder
	ladders = int(inputFile[0].strip("\n"))
	for x in range(0, ladders):
		ladderBottom = int(inputFile[x + 1].split(" ")[0])
		ladderTop = int(inputFile[x + 1].strip("\n").split(" ")[1])
		board[ladderBottom] = ladderTop

	# Get snakes and update board[snake_mouth] to snake_tail
	snakes = int(inputFile[ladders + 1].strip("\n"))
	for x in range(ladders + 1, ladders + 1 + snakes):
		snakeHead = int(inputFile[x + 1].split(" ")[0])
		snakeTail = int(inputFile[x + 1].strip("\n").split(" ")[1])
		board[snakeHead] = snakeTail

	return board

def modifiedDijkstra(N, board, verbose=True):
	# List to maintain if an element has been visited
	isCalled = [0 for i in range(0, N)]

	# List of list of tuples
	# Each tuple has 3 elements: (the board element, list(path to that element from 0), list(dice rolls))
	levels = []
	isCalled[0] = 1
	levels.append([(0, [0], [])])
	# For each level in the list of levels. Go step wise on each level
	for level in levels:
		# Maintain a list of neighbours for all squares (tuples) in a level
		neighbours = []
		for some_tuple in level:
			index, path, dice = some_tuple
			# Add all subsequent 6 elements on the board to neighbours, after computing the list(new path) and list (new dice)
			for x in range (index + 1, index + 7):
				if x <= N-1:
					if not isCalled[board[x]]:
						isCalled[board[x]] = 1
						# Create a new list for path from 0, and add the latest board[x]
						new_path = list(path)
						new_path.append(board[x])
						# Create a new list for dice rolls taken, and add the latest dice roll
						new_dice = list(dice)
						new_dice.append(x - index)
						# Create a new tuple with all the three constituent values
						new_tuple = (board[x], new_path, new_dice)
						# Add the tuple to a list
						neighbours.append(new_tuple)
						if board[x] == N-1:
							a = str(new_path[0])
							for x in range (0, len(new_dice)):
								a += " --[" + str(new_dice[x]) + "]-> " + str(new_path[1 + x])
							if verbose:
								print( "Shortest path is " + str(len(new_dice)) + " steps")
								print( a)
							return
		if neighbours != []:
			# Keep adding the list of neigbour tuples, to levels
			levels.append(neighbours)
	if not isCalled[N-1] and verbose:
		print( "No path found")

if __name__ == "__main__":
	board = createBoard(10001)
	modifiedDijkstra(10001, board)
	
