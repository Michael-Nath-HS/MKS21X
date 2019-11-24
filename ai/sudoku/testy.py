#!/usr/bin/python3
from sys import argv


def something():
    inpt = open(argv[1], "r")
    oupt = open(argv[2], "w")
    id = argv[3]
    inpt = inpt.read().split("\n\n")
    for i in inpt:
        if i.split("\n")[0].split(",")[0] == id:
            nboard = "".join("".join(i.split("\n")[1:]).split(",")).strip()
            break
    print(board)



something()


