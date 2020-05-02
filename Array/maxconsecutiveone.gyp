# Given a binary array, find the maximum number of consecutive 1s in this array.
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
# The maximum number of consecutive 1s is 3.

# Note:
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        # Initialize counter to zero
        count = 0
        result = 0
        
        # Iterate through the array
        for i in nums:
            
            # Reset count when zero is found
            if i == 0:
                count = 0
            
            # If 1 is found, increment count and update
            else:
                count += 1
                result = max(result,count)
        return result
