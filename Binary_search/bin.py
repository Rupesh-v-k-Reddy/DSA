# vanilla Binary search

def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]< target:
            low = mid+1
        else:
            high = mid-1
    return -1

# a=[1,3,6,8,9,10]
# target = 2
# print(binary_search(a,target))

#recursive version of vanilla binary search

def rec_bin_search(arr,target,low,high):
    if(high >= low):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return rec_bin_search(arr,target,mid+1,high)
        else:
            return rec_bin_search(arr,target,low,mid-1)
        return -1
    else:
        return -1

a=[1,3,6,8,9,10]
target = 2
low = 0
high = len(a)-1
print(rec_bin_search(a,target,low,high))

#order agnostic binary search 
#used when we don't whether the array is in ascending or descinding order but we know it's a sorted array


def ord_bin_search(arr,target):
    start = 0
    end = len(arr)-1
    is_ASC = arr[sart] < arr[end]
    while start <= end:
        mid = (sart+end)//2
        if arr[mid] == target:
            return mid
        if is_ASC:
            #normal binary search
        else:
            #reverse binary search
