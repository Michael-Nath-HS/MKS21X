from random import random
counter = 0
i = 0

while counter < 10000:
    a, b, c = random(), random(), random()
    if c < (a + b) and (b < (a + c)) and (a < (b + c)):
        i += 1
    counter += 1
print("Probability: {}".format(i / counter))

