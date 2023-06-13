#all this problems use binary search on sorted arrays

#this is about finding the boundary index in binary search
def first_boolean(arr):
    left, right = 0,len(arr)-1
    boundary_index = -1
    while left <= right:
        mid = (left+right)//2
        if arr[mid]:
            boundary_index = mid
            right = mid-1
        else:
            left = mid+1
    return boundary_index

# a= [False,False,True,True,True]
# print(first_boolean(a))

def first_not_smaller(arr,target):
    left,right = 0,len(arr)-1
    boundary_index = -1
    while left<= right:
        mid = (left+right)//2
        if arr[mid] >= target:
            boundary_index = mid
            right = mid-1
        else:
            left = mid+1
    return boundary_index

# a= [1, 3, 3, 5, 8, 8, 10]
# target = 2
# print(first_not_smaller(a,target))

def first_occurence(arr,target):
    left, right = 0,len(arr)-1
    boundary_index = -1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            boundary_index = mid
            right = mid-1
        elif arr[mid] < target:
            left = mid+1
        #this else condition is to check the other half of the array when the target is grater than the mid element 
        else:
            right = mid -1
    return boundary_index

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3
print(first_occurence(arr,target))
