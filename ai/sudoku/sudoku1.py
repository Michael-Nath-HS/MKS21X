from sys import argv

def solver():
  inpt = open(argv[1], "r")
  outpt = open(argv[2], "w")
  name = argv[3].strip()
  boards = inpt.read().split("\n\n")
  inpt.close()
  ans = []
  for i in boards:
    if i.split("\n")[0] == name:
      ans.append(i)
  print(ans[0])

solver()

