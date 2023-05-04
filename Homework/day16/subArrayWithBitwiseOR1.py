"""

Problem Description
Given an array B of length A with elements 1 or 0. Find the number of subarrays such that the bitwise OR of all the elements present in the subarray is 1.
Note : The answer can be large. So, return type must be long.


Problem Constraints
1 <= A <= 105


Input Format
The first argument is a single integer A.
The second argument is an integer array B.


Output Format
Return the number of subarrays with bitwise array 1.


Example Input
Input 1:
A = 3
B = [1, 0, 1]

Input 2:
A = 2
B = [1, 0]


Example Output
Output 1:
5

Output2:
2


Example Explanation
Explanation 1:
The subarrays are :- [1], [0], [1], [1, 0], [0, 1], [1, 0, 1]
Except the subarray [0] all the other subarrays has a Bitwise OR = 1

Explanation 2:
The subarrays are :- [1], [0], [1, 0]
Except the subarray [0] all the other subarrays has a Bitwise OR = 1

"""

import math 

# A = 3
# B = [1, 0, 1]
A = 5
B = [0,1,0,0,0]
def solve(self, A, B):
    n = 0
    zeroArray = []
    count = 0
    subarrayOfZero = 0
    for i in range(0, len(B)):
        if (B[i] == 0):
            count+= 1
        else:
            zeroArray.append(count)
            count = 0 
        if i == len(B)-1:
            zeroArray.append(count)
    print(zeroArray)
    for i in range(0,len(zeroArray)):
        n = zeroArray[i]
        subarrayOfZero = subarrayOfZero + (n*(n+1))/2
    # print(subarrayOfZero)
    n = len(B)
    totalSubarray = (n*(n+1))/2
    print((math.trunc(totalSubarray-subarrayOfZero)))
    # print(totalSubarray-subarrayOfZero)

solve('data', A, B)