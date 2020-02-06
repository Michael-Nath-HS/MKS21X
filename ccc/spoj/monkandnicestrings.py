# def cmp(i1, i2):
#     val1 = 0
#     val2 = 0
#     for x in i1:
#         val1 += ord(x)
#     for y in i2:
#         val2 += ord(y)
#     return val1 > val2
#
#
# def insert_sort(array):
#     for j in range(1, len(array)):
#         key = array[j]
#         i = j - 1
#         while i >= 0 and cmp(array[i], key):
#             array[i + 1] = array[i]
#             i -= 1
#         array[i + 1] = key
#
#
# arr = []
# relations = dict()
# size = int(input())
# tru = [0 for x in range(size)]
# for z in range(size):
#     a = input()
#     relations[z] = 0
#     arr.append(a)
#
# # insert_sort(arr)
# sor_arr = sorted(arr)
# print(arr)
# i = 0
# while i < len(arr):
#     counter = 0
#     for elem in arr[i::-1]:
#         already = False
#         for j in sor_arr:
#             if j == elem and not already:
#                 counter = 1
#                 break
#             elif j == elem and already:
#                 break
#             if j == arr[i]:
#                 already = True
#     relations[i] = counter
#     i += 1
#
# for x in relations.values():
#     print(x)
# # print(arr)


# n = int(input())
# ar = []
# for i in range(n):
#     ar += [input()]
# for i in range(n):
#     cnt = 0
#     for j in range(i):
#         if ar[j] < ar[i]:
#             cnt += 1
#     print(cnt)


ran = int(input())
ar = [int(x) for x in input().split(" ")]
sar = sorted(ar)
ans = ""
for i in ar:
    for j in range(ran):
        if sar[j] == i:
            ans += str(j) + " "
print(ans)