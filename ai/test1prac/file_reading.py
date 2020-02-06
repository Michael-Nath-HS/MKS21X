# Practice using the heapq library in Python3
# Uses a min-heap
import heapq


def tester():
    inpt = open("heapq.txt", "r")
    names = inpt.read().strip().split("\n")
    heapq.heapify(names)
    for i in range(len(names)):
        print("Prioritized {}: {}".format(i + 1, heapq.heappop(names)))


tester()
