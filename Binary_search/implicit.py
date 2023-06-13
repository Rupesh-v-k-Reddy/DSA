#using binary search on implicitly sorted arrays

def min_in_sorted_array(arr):
    left,right= 0,len(arr)-1
    boundary_index =-1
    while left <=right:
        mid = (left+right)//2
        if arr[mid] <= arr[-1]: #if arr[mid] <= arr[-1] then the target belongs inthe lower half
            boundary_index = mid
            right = mid-1
        else:
            left = mid+1
    return boundary_index

a = [3, 5, 7, 11, 13, 17, 19, 2]
print(min_in_sorted_array(a))

# Find the index of the peak element. Assume there is only one peak element.
# Input: 0 1 2 3 2 1 0
# Output: 3
# Explanation: the largest element is 3 and its index is 3.

def peak_of_mountain array(array):
    left,right = 0, len(arr)-1
    boundary_index =-1
    while left<= right:
        mid = (left+right)//2
        if mid == len(arr)-1 or arr[mid] >= arr[mid+1]:
            boundary_index = mid
            right = mid-1
        else:
            left = mid+1
    return boundary_index

