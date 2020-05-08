# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.

# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
# Internally you can think of this:
# nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
# any modification to nums in your function would be known by the caller.
# using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

# Problem is similar to Remove Element problem.
# The only difference is you are to delete all duplicates in the array so the element will only appear once

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize counter pointer
        counter = 1
        
        # Iterate through nums
        for i in range(1, len(nums)):
            # Check if current value is not equal to previous value
            if nums[i] != nums[i - 1]:
                # If current value is unique, then assign to pointer value
                nums[counter] = nums[i]
                # Increment pointer
                counter += 1
        # Return value of pointer
        return counter
