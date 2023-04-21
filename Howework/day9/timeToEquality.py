"""
Problem Description
Given an integer array A of size N. In one second, you can increase the value of one element by 1.
Find the minimum time in seconds to make all elements of the array equal.


Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 1000


Input Format
First argument is an integer array A.

Output Format
Return an integer denoting the minimum time to make all elements equal.


Example Input
A = [2, 4, 1, 3, 2]

Example Output
8


Example Explanation
We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds.

"""

A = [2, 4, 1, 3, 2]
def solve(self, A):
    largest = -10e9;
    if len(A) > 0:
        i = 0
        while i < len(A):
            if (largest < int(A[i])):
                largest = int(A[i])
            i = i + 1
    time = 0
    for i in range(0, len(A)):
        while A[i] < largest:
            A[i]+=1
            time+=1
    print(time)

solve('data', A)