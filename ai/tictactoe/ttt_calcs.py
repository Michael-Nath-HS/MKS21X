from random import randint, choice


def diff_games():
    clean = "_________"
    counter = 0
    states = set()
    switcher = True
    cur = list(clean)
    x = 0

    while x <= 8:
        print(x)
        cur[x] = "X"
        prev = cur.copy()
        for o in range(9):
            switcher = True
            if cur[o] == "_":
                cur[o] = "O"
            else:
                continue

            while "_" in cur:
                print(cur, switcher)
                if switcher:
                    for i in range(9):
                        if cur[i] == "_":
                            cur[i] = "X"
                            break
                else:
                    for i in range(9):
                        if cur[i] == "_":
                            cur[i] = "O"
                            break

                switcher = not switcher
                states.add("".join(cur))
                counter += 1

            cur = prev.copy()
        cur = list(clean).copy()
        x += 1

    return len(states), counter


print(diff_games())
