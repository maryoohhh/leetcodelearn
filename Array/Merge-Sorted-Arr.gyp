# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

# Example:
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# Output: [1,2,2,3,5,6]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Initialize starting index for nums1
        i = m - 1
        # Initialize starting index for nums2
        j = n - 1
        
        # Initialize total capacity index of nums1
        k = m + n - 1
        
        # Loop until nums1 iterate through index 0
        # Iterating from end-forward
        while k >= 0:
            # Check if we've iterated through nums2
            # Check if an index in nums1 contains 0
            # Check if nums2 is greater than nums1
            if j >= 0 and (m == 0 or nums2[j] >= nums1[i]):
                # Then last index in nums1 is nums2
                nums1[k] = nums2[j]
                j -= 1
            # Check if we've iterated through nums2
            # Check if nums1 is greater than nums2
            elif j > -1 and nums1[i] > nums2 [j]:
                # Then switch placements
                nums1[k], nums1[i] = nums1[i], nums1[k]
                if i: i -=1
            k -= 1
        
