"""
USER: mnath101
LANG: PYTHON3
TASK: gift1
"""

fin = open("gift1.in", "r").read().split("\n")
fout = open("gift1.out", "w")
account = {}
meat = fin[int(fin[0]) + 1:]
for i in fin[1:int(fin[0]) + 1]:
    account[i] = 0

j = int(fin[0]) + 1
while j < len(fin) - 1:
    person = fin[j]
    info = fin[j+1].split(" ")
    if int(info[0]) != 0 and int(info[1]) != 0:
        account[person] = account[person] - int(info[0]) + (int(info[0]) % int(info[1]))
        for i in range(j + 2, j + int(info[1]) + 2):
            account[fin[i]] += int(info[0]) // int(info[1])

    j += int(info[1]) + 2
for i in account.items():
    fout.write("{} {}\n".format(i[0], i[1]))
fout.close()





