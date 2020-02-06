from time import time
def birthday(s, d, m):
	count = 0
	for i in range(len(s)):
		sum = 0
		for j in range(i, i + m):
			if j < len(s):
				sum += s[j]
		if sum == d:
			count += 1
	return count

start = time()
s = [1,2,2,2,3,4,5,5,5,5,5,8,2,2,7,4,2,3,1,2,2,2,3,4,5,5,5,5,5,8,2,2,7,4,2,3,3,1]
d = 4
m = 1
print(birthday(s,d,m))
print(time() - start)

