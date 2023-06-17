# One of the most common applications of a hash table or set is determining if an element exists in O(1). Since an array needs 
# O(n) to do this, using a hash map or set can improve the time complexity of an algorithm greatly, usually from 
# O(n^2) to O(n). Let's look at some example problems

# Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. 
# You cannot use the same index twice

 def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic: # This operation is O(1)!
                return [i, dic[complement]]
            
            dic[num] = i
        
        return [-1, -1]

# Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.

def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "

#  Given an integer array nums, find all the numbers x that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums

def find_numbers(nums):
    ans = []
    nums = set(nums)

    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)
    
    return ans



# Anytime you find your algorithm running if ... in ..., then consider using a hash map or set to store elements to have these operations run in O(1).
