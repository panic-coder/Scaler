"""
Problem Description
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.


Problem Constraints
1 <= A.size() <= 104
1 <= A[i] <= 109
1 <= B <= 109


Input Format
First argument is an integer array A.
Second argument is an integer B.

Output Format
Return 1 if good pair exist otherwise return 0.


Example Input
Input 1:
A = [1,2,3,4]
B = 7

Input 2:
A = [1,2,4]
B = 4

Input 3:
A = [1,2,2]
B = 4


Example Output
Output 1:
1

Output 2:
0

Output 3:
1


Example Explanation
Explanation 1:
 (i,j) = (3,4)

Explanation 2:
No pair has sum equal to 4.

Explanation 3:
 (i,j) = (2,3)

"""

# A = [1,2,3,4]
# B = 7
A = [1,2,4]
B = 4
def solve(self, A, B):
    n = len(A)
    i = 0
    count = 0
    while i < n-1:
        j = i+1
        while j < n:
            if A[i] + A[j] == B:
                count+=1
                break
            j+=1
        i+=1
    if count > 0:
        print(1)
    else:
        print(0)
    # return array
    # print(array)

solve('data', A, B)