# Valid Mountain Array

# Given an array A of integers, return true if and only if it is a valid mountain array.

# Recall that A is a mountain array if and only if:

# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        if (len(A) < 3): return False
        
        i = 1
        while (i<len(A) and A[i]>A[i-1]):
            i += 1
        if(i==1 or i==len(A)):
            return False
        while(i<len(A) and A[i]<A[i-1]):
            i += 1
        return i==len(A)
