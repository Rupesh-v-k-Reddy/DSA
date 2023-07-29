# Given an array of integers sorted in ascending order, find two numbers that add up to a given target. 
#Return the indices of the two numbers in ascending order. You can assume elements in the array are unique and there is only one solution. 
#Do this in O(n) time and with constant auxiliary space.
# Input: [2 3 4 5 8 11 18], 8
# Output: 1 3

def two_sum(arr,target):
    left =0
    right =len(arr)-1
    while left <= right:
        current_sum = arr[left]+arr[right]
        if current_sum == target:
            return left,right
        elif current_sum > target:
            right -=1
        else:
            left +=1
    return -1


#reverse a string 
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
def string_reversal(s:List[str])->str:
    left = 0
    right = len(s)-1
    while left <= right:
        s[left],s[right] = s[right],s[left]
    return s


# check if the string is palindrome
def palindrome(s:str)->None:
    left = 0
    right= len(s)-1
    while left <= right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True