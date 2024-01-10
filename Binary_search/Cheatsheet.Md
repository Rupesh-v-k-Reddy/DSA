### Implementation Template

```python
def bin_search(arr,target){
    left =0
    right = len(arr)-1
    while left <= right:
        mid = (left+right) //2
        if arr[mid] == target:
            #do something
            return
        if arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    # target is not in arr, but left is at the insertion point
    return left
}
```


### Duplicate Elements

```python
def bin_search(arr,target):
    left = 0
    right -len(arr)-1
    while left < right:
        mid = (left+right)//2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid+1
    return left
```

The following template will find the right-most insertion point (the index of the right-most element plus one):
```python
def bin_search(arr,target):
    left = 0 
    right = len(arr)-1
    while left < right:
        mid = (left+right) //2
        if arr[mid] > target:
            right = mid
        else:
            left = mid +1
    return left
```

Regarding both of the above templates, if the element you are searching for does not exist, then left will be at the index where the element should be inserted to maintain sorted order (just like in a normal binary search)

## On Arrays
You are given an array of integers nums which is sorted in ascending order, and an integer target. If target exists in nums, return its index. Otherwise, return -1.
```python
def bin_search(arr,target):
    left =0
    right = len(arr) -1
    while left <= right:
        mid = (left+ right)//2
        num = arr[mid]
        if num == target:
            return num
        elif num > target:
            right = mid-1
        else:
            left = mid +1
    return -1
```

### search a 2d matrix
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row

Because each row is sorted and fully less than the next row, we can treat the matrix as one array. This hypothetical single array has a length of m * n. If we consider the indices between [0, m * n - 1], then how do we find the row and column that each index converts to?

Each row has n elements. That means that row 0 is indices [0, n - 1]. Row 1 is indices [n, 2 * n - 1], and so on. This is equivalent to the floor division of n, aka row = i // n - the row increments every n indices

The column can range between [0, n - 1]. Every n indices, the column resets to 0. This is perfect for the modulo operator. col = i % n.

```python
def bin_Search(arr,target):
    m,n = len(arr),len(arr[0])
    left , right = 0, m*n-1
    while left < right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        num = arr[row][col]

        if num == target:
            return True
        if num < target:
            left = mid+1
        else:
            right = mid-1
    return False
```

