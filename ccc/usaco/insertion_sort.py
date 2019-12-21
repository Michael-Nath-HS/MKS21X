from random import randint
# insert_sort: performs insertion sort on an array of integers


def insert_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key

    return array

# rev_insert: sorts an array of integers in order of greatest to least


def rev_insert(a):

    # create a for loop that will contain an iterator
    for j in range(1, len(a)):
        # create a temporary key that dedicates current element that you are focusing on.
        key = a[j]
        # because we're essentially thinking of this as picking a card and comparing to cards to the left of it,
        # we want i to work leftward.
        i = j - 1
        while i >= 0 and a[i] < key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key

    return a


def linear_search(arr, elem):
    # loop invariant: [0, j]
    # before loop, j = 0. [0,0] is just the first element and it'll return true or false
    # if the only element is the element desired.

    for j in range(0, len(arr)):
        if arr[j] == elem:
            return j
    return None


a = [randint(1, 100) for x in range(15)]
b = randint(1, 100)

print("Original Array: {}".format(a))
print("Least to Greatest: {}".format(insert_sort(a)))
print("Greatest to Least: {}".format(rev_insert(a)))
print("{} in array: {}".format(b, linear_search(a, b)))
