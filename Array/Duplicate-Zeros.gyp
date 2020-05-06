# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Example 1:
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Note:
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # Initialize i counter
        i = 0
        
        # Loop all elements in array
        while i < len(arr) - 1:
            # check if an element is zero
            if (arr[i] == 0):
                # Remove last element in the Array
                arr.pop()
                # Insert zero in i + 1 placement
                arr.insert(i + 1, 0)
                # Shift placement
                i += 1
                
            # Increment to next index
            i += 1
            
