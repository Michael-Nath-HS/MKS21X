
class SudokuCell:
    def __init__(self, val, data, row, column, square):
        self.val = val
        self.data = data
        self.info = {data: [row, column, square]}

# we recieve a "solved" board and want to verify that is indeed solved
# we take all 3 cliques for a given cell and set that as attributes for that cell object
# we try and see if the intersection of each clique (in type list) and its set are equivalent
# if they are, then each clique is valid.

class SudokuBoard:
    def __init__(self):
        self.rowa = []
        self.columna = []
        self.squarea = []
        self.array = []
        self.cliques = [[0, 1, 2, 3, 4, 5, 6, 7, 8], \
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

    def verify(self):
        from sys import argv
        inpt = open(argv[1], "r")
        cells = ",".join(inpt.read().split("\n")[1:]).split(",")
        for i in range(len(cells)):
            row = i // 9
            nrow = [cells[i] for i in self.cliques[row]]
            column = (i % 9)
            ncolumn = [cells[i] for i in self.cliques[column + 9]]
            square = (column // 3) + (3 * (row // 3))
            nsquare = [cells[i] for i in self.cliques[square + 18]]
            node = SudokuCell(cells[i], str(i), nrow, ncolumn, nsquare)
            self.array.append(node)

        for i in self.array:
            print(type(i.data))
            if sorted(i.info[i.data][0]) != sorted(list(set(i.info[i.data][0]))):
                self.rowa.append(i.val)
            if sorted(i.info[i.data][1]) != sorted(list(set(i.info[i.data][1]))):
                self.columna.append(i.val)
            if sorted(i.info[i.data][2]) != sorted(list(set(i.info[i.data][2]))):
                self.squarea.append(i.val)

            continue

        return "Incorrectly Solved Board. Positions: {}\n{}\n{}".format(self.rowa, self.columna, self.squarea)
        return "Board is correctly Solved"
        inpt.close()
        return cells

myboard = SudokuBoard()
print(myboard.verify())

