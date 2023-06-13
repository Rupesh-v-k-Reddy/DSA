# Given a sorted list of numbers, remove duplicates and return the new length. You must do this in-place and without using extra memory.

# Input: [0, 0, 1, 1, 1, 2, 2].

# Output: 3.


def remove_duplicates(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] !== arr[slow]:
            slow +=1
            arr[slow] = arr[fast]
    return slow+1

# Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of the non-zero elements. 
# Do this in-place using constant auxiliary space.
# Input : [1, 0, 2, 0, 0, 7]
# Output: [1, 2, 7, 0, 0, 0]

def non_zero(arr):
    slow= 0 
    for fasat in range(len(arr)):
        if arr[fast]!= 0:
            arr[slow],arr[fast] = arr[fast],arr[slow]
            slow +=1
    return arr