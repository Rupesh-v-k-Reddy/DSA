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