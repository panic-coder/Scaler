"""
Problem Description
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.


Problem Constraints
1 <= |A| <= 105
0 <= A[i] <= 109


Input Format
The first argument is an integer array A.

Output Format
Return the second largest element. If no such element exist then return -1.


Example Input
Input 1:
 A = [2, 1, 2] 

Input 2:
 A = [2]


Example Output
Output 1:
 2 

Output 2:
 -1 


Example Explanation
Explanation 1:
 First largest element = 2
 Second largest element = 2
 Third largest element = 1

Explanation 2:
 There is no second largest element in the array.

"""

# A = [2, 10, 3, 1, 5]
A = [2]
def solve(self, A):
    print('self ',self)
    largest = A[0];
    secondLargest = A[0]
    i = 1
    n = len(A)
    if n > 1:
        while i < n:
            # print('i+1 : ',A[i+1])
            if largest < A[i]:
                secondLargest = largest
                largest = A[i]
            elif( (secondLargest < A[i]) and (largest != A[i]) ):
            # if( (secondLargest < A[i+1]) ):
                secondLargest = A[i]
            print('i+1 : ',A[i])
            print('Largest : ',largest)
            print('Second Largest : ',secondLargest)
            print()
            i = i + 1
        # print('Largest : ',largest)
        # print('Second Largest : ',secondLargest)
    else:
        print(-1)


solve('data', A)