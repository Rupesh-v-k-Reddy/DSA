# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def moveZeroes(self, nums: List[int]) -> None:
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.append(0)

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.


def isSubsequence(self, s: str, t: str) -> bool:
    if s == "":
        return True
    if t == "":
        return False
    i = 0
    for j in range(len(t)):
        if t[j] == s[i]:
            i += 1
            if i == len(s):
                return True
    return i == len(s)


# container with most water leetcode

def maxArea(height):
    left = 0
    right = len(height)-1
    max_water = 0
    while left < right:
        area = (right-left)*min(height[left], height[right])
        max_water = max(area, max_water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


# trapping rain water leetcode

def trap(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax-height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax-height[r]
    return res
