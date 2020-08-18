# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
# More formally check if there exists two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()

        for i in arr:
        	# Checks if i * 2 is in the s list
            if i * 2 in s: return True
            # Checks if i is divisible by 2 and if the quotient is in the s list 
            if i % 2 == 0 and int(i/2) in s: return True
            # add i in the s list
            s.add(i)
        return False
