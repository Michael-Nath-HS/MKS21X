#! /usr/bin/python3

def unswap():
    Cliques = [[0, 1, 2, 3, 4, 5, 6, 7, 8], \
               [9, 10, 11, 12, 13, 14, 15, 16, 17], \
               [18, 19, 20, 21, 22, 23, 24, 25, 26], \
               [27, 28, 29, 30, 31, 32, 33, 34, 35],
               [36, 37, 38, 39, 40, 41, 42, 43, 44],
               [45, 46, 47, 48, 49, 50, 51, 52, 53], \
               [54, 55, 56, 57, 58, 59, 60, 61, 62], \
               [63, 64, 65, 66, 67, 68, 69, 70, 71], \
               [72, 73, 74, 75, 76, 77, 78, 79, 80, ], \
               [0, 9, 18, 27, 36, 45, 54, 63, 72], \
               [1, 10, 19, 28, 37, 46, 55, 64, 73], \
               [2, 11, 20, 29, 38, 47, 56, 65, 74],
               [3, 12, 21, 30, 39, 48, 57, 66, 75], \
               [4, 13, 22, 31, 40, 49, 58, 67, 76], \
               [5, 14, 23, 32, 41, 50, 59, 68, 77], \
               [6, 15, 24, 33, 42, 51, 60, 69, 78], \
               [7, 16, 25, 34, 43, 52, 61, 70, 79], \
               [8, 17, 26, 35, 44, 53, 62, 71, 80], \
               [0, 1, 2, 9, 10, 11, 18, 19, 20], \
               [3, 4, 5, 12, 13, 14, 21, 22, 23], \
               [6, 7, 8, 15, 16, 17, 24, 25, 26], \
               [27, 28, 29, 36, 37, 38, 45, 46, 47], \
               [30, 31, 32, 39, 40, 41, 48, 49, 50], \
               [33, 34, 35, 42, 43, 44, 51, 52, 53], \
               [54, 55, 56, 63, 64, 65, 72, 73, 74], \
               [57, 58, 59, 66, 67, 68, 75, 76, 77], \
               [60, 61, 62, 69, 70, 71, 78, 79, 80]
               ]
    import sys
    inpt = open(sys.argv[1], "r")
    outpt = open(sys.argv[2], "w")

    boards = inpt.read().strip().split("\n\n")
    i = 1
    for theboard in boards:
        board = []
        lines = theboard.split("\n")
        for line in lines[1:]:
            values = line.split(",")
            for value in values:
                board.append(int(value))

        rows = Cliques[0:9]
        columns = Cliques[9:18]
        squares = Cliques[18:]

        problemRows = []
        problemColumns = []
        problemSquares = []


        for square in squares:
            numbers = set()
            for num in square:
                numbers.add(board[num])
            if len(numbers) != 9:
                for num in square:
                    problemSquares.append(num)
        for column in columns:
            numbers = set()
            for num in column:
                numbers.add(board[num])
            if len(numbers) != 9:
                for num in column:
                    problemColumns.append(num)
        for row in rows:
            numbers = set()
            for num in row:
                numbers.add(board[num])
            if len(numbers) != 9:
                for num in row:
                    problemRows.append(num)

        problem = {x for x in range(81)}
        if len(problemRows) != 0:
            problem = problem.intersection(problemRows)

        if (problemColumns) != 0:
            problem = problem.intersection(problemColumns)

        if len(problemSquares) != 0:
            problem = problem.intersection(problemSquares)

        if len(problem) == 2:
            problem = sorted(list(problem))
            outpt.write("{},{}\n".format(problem[0], problem[1]))

        else:
            checker = True
            problem = list(problem)
            for pos in range(len(problem) - 1):
                if checker:
                    for num in range(pos, len(problem)):
                        boardcopy = board.copy()
                        pos1 = problem[pos]
                        num1 = problem[num]
                        boardcopy[pos1], boardcopy[num1] = boardcopy[num1], boardcopy[pos1]
                        solved = True
                        for elem in Cliques:
                            numbers = set()
                            for elemy in elem:
                                    numbers.add(boardcopy[elemy])
                            if len(numbers) != 9:
                                solved = False
                                break
                        if solved:
                            ans = sorted([pos1, num1])
                            outpt.write("{},{}\n".format(ans[0], ans[1]))
                            checker = False

        i += 1;

unswap()