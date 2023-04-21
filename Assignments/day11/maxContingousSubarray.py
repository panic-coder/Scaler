"""
Problem Description
Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.


Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000


Input Format
The first and the only argument contains an integer array, A.

Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.


Example Input
Input 1:
 A = [1, 2, 3, 4, -10] 

Input 2:
 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 


Example Output
Output 1:
 10 

Output 2:
 6 


Example Explanation
Explanation 1:
 The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 

Explanation 2:
 The subarray [4,-1,2,1] has the maximum possible sum of 6. 

"""

# A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
A = [ -163, -20 ]

def maxSubArray(self, A):
    max =A[0]
    currentMax = A[0]
     
    for i in range(1,len(A)):
        currentMax = max(A[i], currentMax + A[i])
        max = max(max,currentMax)
         
    # return max
    print(max)

    

maxSubArray('data', A)