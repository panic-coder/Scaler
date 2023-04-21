"""

Problem Description
Given an Array of size N, find the subArray of size K with the least average.


Problem Constraints
1<=k<=N<=1e5
-1e5<=A[i]<=1e5


Input Format
First argument contains an Array A of integers of size N.
Second argument contains integer k.

Output Format
Return the index of the first element of the subArray of size k that has least average.
Aay indexing starts from 0.


Example Input
Input 1:
A=[3, 7, 90, 20, 10, 50, 40]
B=3

Input 2:
A=[3, 7, 5, 20, -10, 0, 12]
B=2


Example Output
Output 1:
3

Output 2:
4


Example Explanation
Explanation 1:
SubArray between indexes 3 and 5
The subArray {20, 10, 50} has the least average 
among all subArrays of size 3.

Explanation 2:
 SubAay between [4, 5] has minimum average

"""

# A=[3, 7, 90, 20, 10, 50, 40]
# B=3
A = [ 18, 11, 16, 19, 11, 9, 8, 15, 3, 10, 9, 20, 1, 19 ]
B = 1
def solve(self, A, B):
    k = B
    n = len(A)
    if n < k:
        return 0
    resIndex = 0
    currentSum = 0
    for i in range(k):
        currentSum += A[i]
    minSum = currentSum
    print("minSum", minSum)

    for i in range(k, n):
        currentSum += A[i] - A[i - k]
        print("currentSum {index}".format(index=i), currentSum)
        print()
        if (currentSum < minSum):
            print("INSIDE IF...")
            minSum = currentSum
            print("NEW minSum", minSum)
            resIndex = (i - k + 1)
            print("NEW resIndex", resIndex)
            print()
        
    print(resIndex)

solve('data', A, B)