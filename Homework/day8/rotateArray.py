"""
Problem Description
Given an array of integers A and multiple values in B, which represents the number of times array A needs to be left rotated.
Find the rotated array for each value and return the result in the from of a matrix where ith row represents the rotated array for the ith value in B.


Problem Constraints
1 <= length of both arrays <= 2000 -10^9 <= A[i] <= 10^9 0 <= B[i] <= 2000


Input Format
The first argument given is the integer array A.
The second argument given is the integer array B.

Output Format
Return the resultant matrix.


Example Input
Input 1:
     A = [1, 2, 3, 4, 5]
    B = [2, 3]

Input 2:
    A = [5, 17, 100, 11]
    B = [1]


Example Output
Output 1:
 [ [3, 4, 5, 1, 2]
    [4, 5, 1, 2, 3] ]

Output 2:
[ [17, 100, 11, 5] ]


Example Explanation
for input 1 -> B[0] = 2 which requires 2 times left rotations
1: [2, 3, 4, 5, 1]
2: [3, 4, 5, 1, 2]

B[1] = 3 which requires 3 times left rotation
1: [2, 3, 4, 5, 1]
2: [3, 4, 5, 1, 2]
2: [4, 5, 1, 2, 4]

"""

A = [1, 2, 3, 4, 5]
B = [2, 3]
def solve(self, A, B):
    def swap(a, b, i, j, C):
        C[i] = b
        C[j] = a
        return C

    def reverse(C, s, e):
        i = s
        j = e
        while i<j:
            C = swap(C[i], C[j], i, j, C);
            i+=1
            j-=1
        return C
    outerLoop = 0
    n = len(A)
    C = []
    outputArray = []
    while outerLoop < len(B):
        # print('outer loop : ',outerLoop)
        C = A[:]
        # print("C outer ", C)
        K = B[outerLoop]
        if K >= n:
            K = K%n
        
        C = reverse(C, 0, K-1);
        C = reverse(C, K, n-1);
        C = reverse(C, 0, n-1);
        # print("C end", C)
        # print()
        outputArray.append(C)
        outerLoop+=1
        # return outputArray
    return outputArray
# print(outputArray)


solve('data', A, B)