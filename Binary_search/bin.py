#Binary search


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

a=[1,3,6,8,9,10]
target = 2
print(binary_search(a,target))