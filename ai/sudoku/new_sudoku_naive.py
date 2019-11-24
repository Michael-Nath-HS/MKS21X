#! /usr/bin/python3
import sys
import time

def solver():
    tim = time.time()
    big_dict = {}
    # This has all the rows, columns, and squares that a given cell is a part of
    Cliques = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24, 25, 26],
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
    # Read in the input sudoku file
    inpt = open(sys.argv[1], "r")
    # The output sudoku file
    oupt = open(sys.argv[2], "w+")
    # ID of the sudoku board in the sudoku file
    id = sys.argv[3]
    inpt = inpt.read().split("\n\n")
    for i in inpt:
        if i.split("\n")[0].split(",")[0] == id:
            nboard = "".join("".join(i.split("\n")[1:]).split(",")).strip()
            break
    # Manufacture the board as an easy-to-manipulative string
    ultspots = set()
    for i in range(81):
        row = i // 9
        column = i % 9
        square = (column // 3) + (3 * (row // 3))
        neighborhood = set()
        for elem in Cliques[row]:
            neighborhood.add(elem)
        for elem in Cliques[column + 9]:
            neighborhood.add(elem)
        for elem in Cliques[square + 18]:
            neighborhood.add(elem)
        # Create a mega dictionary that stores the "neighborhood" as the value of a given position (which becomes the key)
        big_dict[i] = list(neighborhood)

        if nboard[i] == "_":
            numbers = set()
            ultspots.add(i)
            for j in big_dict[i]:
                if nboard[j] != "_":
                    numbers.add(int(nboard[j]))
        else:
            continue

    count = 0
    ultspots = sorted(ultspots)
    spot = ultspots[count]
    latest_version = list(nboard)
    newultspots = []
    for i in range(len(ultspots)):
        all_vals = [latest_version[j] for j in big_dict[ultspots[i]] if j != ultspots[i] and latest_version[j] != "_"]
        numstry = sorted(list({"1", "2", "3", "4", "5", "6", "7", "8", "9"}.difference(set(all_vals))))
        if len(numstry) == 1:
            latest_version[ultspots[i]] = str(ultspots[i])

        else:
            newultspots.append(ultspots[i])

    backtrack = []
    boardsolve(big_dict, newultspots, spot, latest_version, backtrack, {spot})
    ans = ""
    county = 0
    for i in latest_version:
        if county % 9 == 8:
            ans += "{}\n".format(i)
        else:
            ans += "{},".format(i)
        county += 1
    print(ans)
    oupt.write("\n\n" + ans + "\n\n")
    oupt.write("Time taken: {}".format(time.time() - tim) + "\n\n")
    oupt.write("Amount of Backtracks: {}".format(sum(backtrack)) + "\n\n")
    print("Time taken: {}".format(time.time() - tim))
    print("Amount of Backtracks: {}".format(sum(backtrack)))


def boardsolve(dicty, source, cell, board, counter, prevCells):
    all_vals = [board[j] for j in dicty[cell] if j != cell and board[j] != "_"]
    numstry = sorted(list({"1", "2", "3", "4", "5", "6", "7", "8", "9"}.difference(set(all_vals))))
    min = 9
    ncell = -1

    for i in numstry:
        if str(i) not in all_vals:
            board[cell] = str(i)
            for z in source:
                if z not in prevCells:
                    new_vals = [board[j] for j in dicty[z] if j != z and board[j] != "_"]
                    new_numstry = sorted(list({"1", "2", "3", "4", "5", "6", "7", "8", "9"}.difference(set(new_vals))))
                    if len(new_numstry) < min:
                        min = len(new_numstry)
                        ncell = z
            prevCells.add(ncell)
            if "_" not in board:
                return True
            if boardsolve(dicty, source, ncell, board, counter, prevCells):
                return True
            else:
                prevCells.remove(ncell)
                counter.append(1)
                board[cell] = "_"
    return False

solver()
