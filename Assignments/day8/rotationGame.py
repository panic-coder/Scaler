"""
Problem Description
Given an integer array A and an integer B, you have to print the same array after rotating it B times towards the right.

NOTE: You can use extra memory.


Problem Constraints
1 <= |A| <= 106
1 <= A[i] <= 109
1 <= B <= 109


Input Format
The first line begins with an integer A denoting the length of an array, and then A integers represent the array elements.
The second line contains a single integer B

Output Format
Print an array of integers which is the Bth right rotation of input array A, on a separate line.


Example Input
Input 1:
 4 1 2 3 4
 2

Input 2:
 3 1 2 2
 3


Example Output
Output 1:
 3 4 1 2

Output 2:
 1 2 2


Example Explanation
Explanation 1:
 [1,2,3,4] => [4,1,2,3] => [3,4,1,2]

Explanation 2:
 [1,2,2] => [2,1,2] => [2,2,1] => [1,2,2]

"""

# A = [4, 1, 2, 3, 4]
# 2]
def solve(self):
    def swap(a, b, i, j, C):
        C[i] = b
        C[j] = a
        return C

    def reverse(C, s, e):
        i = s
        j = e
        while i<j:
            C = swap(int(C[i]), int(C[j]), i, j, C);
            i+=1
            j-=1
        return C
    A = input().split()
    A.pop(0)
    B = int(input())
    # outerLoop = 0
    n = len(A)
    C = []
    outputArray = []
    # while outerLoop < len(B):
    # print('outer loop : ',outerLoop)
    C = A[:]
    # print("C outer ", C)
    K = B
    if K >= n:
        K = K%n
    C = reverse(C, 0, n-1);
    C = reverse(C, 0, K-1);
    C = reverse(C, K, n-1);
    
    print("C end", C)
    # print()
    outputArray = C
        # outerLoop+=1
        # return outputArray
    # return outputArray
    # print(outputArray)
    for i in range(0, len(outputArray)):
        print(outputArray[i], end = " ")

solve('data')