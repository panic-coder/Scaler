"""

Problem Description
You are given two integer matrices A(having M X N size) and B(having N X P). You have to multiply matrix A with B and return the resultant matrix. (i.e. return the matrix AB).

image



Problem Constraints
1 <= M, N, P <= 100

-100 <= A[i][j], B[i][j] <= 100



Input Format
There are 2 lines in the input
First line: Two integers R, C are the number of rows and columns. Then R * C integers follow corresponding to the rowwise numbers in the 2D array.
Second line: Two integer R, C are the number of rows and columns. Then R * C integers follow corresponding to the rowwise numbers in the 2D array.


Output Format
Return a 2D integer matrix denoting AB.



Example Input
Input 1:
2 2 1 2 3 4
2 2 5 6 7 8

Input 2:
1 2 1 1
2 1 2 3


Example Output
Output 1:
 [[19, 22],
  [43, 50]]

Output 2:
 [[5]]


Example Explanation
Explanation 1:
 image

Explanation 2:
 [[1, 1]].[[2, 3]] = [[1 * 2 + 1 * 3]] = [[5]]

"""

A = [ 2, 2, 1, 2, 3, 4 ]
B = [ 2, 2, 5, 6, 7, 8 ]

def solve(self, A, B):
    M = len(A)
    N = len(A[0])
    P = len(B[0])

    C = []

    for i in range(0,M):
        C.append([0] * P)

    for i in range(0, M):
        for j in range(0,P):
            for k in range(0,N):
                C[i][j] = C[i][j] + (A[i][k] * B[k][j])
    # arrayA = []
    # valueAssignIndex = 2
    # i = 0
    # for i in range(A[0]):
    #     subArray = []
    #     for j in range(A[1]):
    #         subArray.append(A[valueAssignIndex])
    #         valueAssignIndex = valueAssignIndex + 1
    #     arrayA.append(subArray)

    # arrayB = []
    # valueAssignIndex = 2
    # for i in range(B[0]):
    #     subArray = []
    #     for j in range(B[1]):
    #         subArray.append(B[valueAssignIndex])
    #         valueAssignIndex = valueAssignIndex + 1
    #     arrayB.append(subArray)

    # print(arrayA)
    # print(arrayB)
    # result = []
    # for i in range(len(arrayA)):
    #     subResultArray = []
    #     for j in range(len(arrayB[0])):
    #         value = 0
    #         for k in range(len(arrayB)):
    #             value = value + ((arrayA[i][k]) * (arrayB[k][j]))
    #         subResultArray.append(value)
    #     result.append(subResultArray)
    # print(result)
solve('data', A, B)