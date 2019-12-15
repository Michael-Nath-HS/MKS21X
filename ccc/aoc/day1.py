def part1():
    ans = 0
    inpt = open("day1.txt", "r").read().strip().split('\n')
    nums = [int(x) for x in inpt]

    for i in nums:
        ans += ((i // 3) - 2)
    return ans

def part2(sum1):
    ans = []
    while sum1 > 0:
        if ((sum1 // 3) - 2) > 0:
            ans.append(((sum1 // 3) - 2))
        sum1 = (sum1 // 3) - 2
    return sum(ans)

def part2answer():
    ans = 0
    inpt = open("day1.txt", "r").read().strip().split('\n')
    nums = [int(x) for x in inpt]
    for i in nums:
        ans += part2(i)
    return ans

print(part2answer())
print(part2(part1()))