"""
Problem Description
Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.


Problem Constraints
1 <= n <= 105
-105 <= A[i] <= 105


Input Format
First argument contains an array A of integers of size N

Output Format
Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.


Example Input
Input 1:
A=[2, 1, 6, 4]

Input 2:
A=[1, 1, 1]


Example Output
Output 1:
1

Output 2:
3


Example Explanation
Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
Therefore, the required output is 1. 

Explanation 2:
Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Therefore, the required output is 3.

"""

A=[2, 1, 6, 4]
def solve(self, A):
    # print(A)
    prefixSumEven = []
    prefixSumEven.append(A[0])
    print("prefixSumEven", prefixSumEven)
    prefixSumOdd = []
    prefixSumOdd.append(0)
    print("prefixSumOdd", prefixSumOdd)

    for i in range(1, len(A)):
        if i%2 == 1:
            prefixSumEven.append(prefixSumEven[i-1])
        else:
            prefixSumEven.append(A[i] + prefixSumEven[i-1])
        if i%2 == 0:
            prefixSumOdd.append(prefixSumOdd[i-1])
        else:
            prefixSumOdd.append(A[i] + prefixSumOdd[i-1])
    print("prefixSumEven", prefixSumEven)
    print("prefixSumOdd", prefixSumOdd)
    count = 0
    n = len(A)
    # i = 0
    for i in range(0,n):
        print("i", i)
        A.pop(i)
        oddIndexed = prefixSumOdd[i-1] + (prefixSumEven[n-1] - prefixSumEven[i])
        evenIndexed = prefixSumEven[i-1] + (prefixSumOdd[n-1] - prefixSumOdd[i])
        if oddIndexed == evenIndexed:
            count+=1
        n = len(A)
        print("len(A)", len(A))
    print(count)
    
solve('data', A)