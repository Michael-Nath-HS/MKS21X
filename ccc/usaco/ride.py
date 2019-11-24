"""
ID: mnath101
LANG: PYTHON3
TASK: ride
"""
import sys

fin = open("ride.in", "r").read().split()
fout = open("ride.out", "w")
comet = fin[0]
group = fin[1]
iter = [comet,group]
prod1 = 1
prod2 = 1
for i in comet:
    prod1 *= (ord(i) - 64)
for i in group:
    prod2 *= (ord(i) - 64)

if (prod1 % 47) == (prod2 % 47):
    fout.write("GO" + "\n")
else:
    fout.write("STAY" + "\n")

sys.stderr.write("{}{}".format(comet, group))