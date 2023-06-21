# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
# A pangram is a sentence where every letter of the English alphabet appears at least once.
 
 def pangram(s):
    seen = set(s)
    return len(seen) == 26

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

# Input: sentence = "leetcode"
# Output: false


# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

def countElements(n):
    seen =set(n)
    count = 0
    for i in n:
        if i+1 in seen:
            count +=1
    return count

# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

# Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.