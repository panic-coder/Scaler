"""
Problem Description
You are given an array of integers A of size N.
Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.


Problem Constraints
2 <= N <= 1e5
-1e9 <= A[i] <= 1e9
There is atleast 1 odd and 1 even number in A


Input Format
The first argument given is the integer array, A.

Output Format
Return maximum among all even numbers of A - minimum among all odd numbers in A.


Example Input
Input 1:
 A = [0, 2, 9]

Input 2:
 A = [5, 17, 100, 1]


Example Output
Output 1:
-7

Output 2:
99


Example Explanation
Explanation 1:
Maximum of all even numbers = 2
Minimum of all odd numbers = 9
ans = 2 - 9 = -7

Explanation 2:
Maximum of all even numbers = 100
Minimum of all odd numbers = 1
ans = 100 - 1 = 99

"""

A = [-98, 54, -52, 15, 23, -97, 12, -64, 52, 85]
def solve(self, A):
    print(A)
    largest = -10e9;
    smallest = 10e9
    i = 1
    n = len(A)
    if n > 1:
        while i < n:
            print('Iteration : ',i)
            print('Largest : ',largest)
            print(' A[i] : ', A[i])
            print()

            # if (A[i] % 2 == 0 and largest < A[i] or (A[i] > 0 and A[i] % 2 == 0)):
            if (A[i] % 2 == 0 and largest < A[i]):
                # smallest = largest
                # if A[i] % 2 == 0:
                largest = A[i]
            # print('smallest > A[i] : ',smallest > A[i])
            # print('Iteration : ',i)
            print('smallest : ',smallest)
            print(' A[i] : ', A[i])
            print()
            # if( (A[i] % 2 != 0 and smallest > A[i]) or (A[i] > 0 and A[i] % 2 != 0) ):
            if( (A[i] % 2 != 0 and smallest > A[i])):
                smallest = A[i]
            print('i : ',A[i])
            print('Largest : ',largest)
            print('Smallest : ',smallest)
            print()
            print()
            i = i + 1
        print('largest - smallest : ',largest - smallest);
        # print('Largest : ',largest)
        # print('Second Largest : ',smallest)
    else:
        print(-1)


solve('data', A)