from math import floor


def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    medpos = floor((m + n) / 2)
    lindex = 0
    rindex = 0
    total = lindex + rindex
    while total < medpos:
        if nums1[lindex] < nums2[rindex]:
            lindex += 1
        elif nums1[lindex] > nums2[rindex]:
            rindex += 1
        else:
            lindex += 1
        total = lindex + rindex
    print(lindex, rindex)
    if lindex < rindex:
        return nums1[lindex]
        print("lindex")
    elif lindex == rindex:
        if nums1[lindex] < nums2[rindex]:
            return nums1[lindex]
        else:
            return nums2[rindex]
    return nums2[rindex]



print(findMedianSortedArrays([1, 5, 7, 11, 15], [2, 4, 9, 10]))
