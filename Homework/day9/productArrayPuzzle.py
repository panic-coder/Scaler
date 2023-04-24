"""
Problem Description
Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.

NOTE: It is always possible to form the product array with integer (32 bit) values.


Input Format
The only argument given is the integer array A.

Output Format
Return the product array.

Constraints
1 <= length of the array <= 1000
1 <= A[i] <= 10

For Example
Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    [120, 60, 40, 30, 24]

Input 2:
    A = [5, 1, 10, 1]
Output 2:
    [10, 50, 5, 50]

"""

A = [1, 2, 3, 4, 5]
def solve(self, A):
    i = 0
    factorial = 1
    while i < len(A):
        factorial = factorial * A[i]
        i+=1
    productArray = []
    i = 0
    while i < len(A):
        productArray.append(int(factorial/A[i]))
        i+=1
    print(*productArray)

solve('data', A)