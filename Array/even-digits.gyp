# Find numbers with even number of digits
# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

# Constraints:

# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5

class Solution(object):
    def findNumbers(self, nums):
        
        # Initialize counter to zero
        counter = 0
        length = 0
        
        # Iterate thru nums
        for i in nums:
            # Count the number of digits a number has
            length = len(str(abs(i)))
            
            # Check and update counter if number of digits is even
            if (length % 2 == 0):
                counter += 1
        return counter
