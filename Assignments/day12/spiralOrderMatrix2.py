"""
Problem Description
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.


Problem Constraints
1 <= A <= 1000


Input Format
First and only argument is integer A

Output Format
Return a 2-D matrix which consists of the elements in spiral order.


Example Input
Input 1:
1

Input 2:
2

Example Output
Output 1:
[ [1] ]

Output 2:
[ [1, 2], [4, 3] ]


Example Explanation
Explanation 1:
 Only 1 is to be arranged.

Explanation 2:
1 --> 2
      |
      |
4<--- 3

"""

A = 2

def solve(self, A):
    n = A
    row1 = 0
    col1 = 0
    row2 = n
    col2 = n
    result = [ [0 for i in range(n)] for j in range(n)]
    num = 1
    while num<=n**2:
        for i in range(col1,col2):
            result[row1][i] = num
            num+=1
        if num > n**2:
            break
        for i in range(row1+1,row2):
            result[i][col2-1] = num
            num+=1
        if num > n**2:
            break
        for i in range(col2-2,col1-1,-1):
            result[row2-1][i] = num
            num+=1
        if num > n**2:
            break
        for i in range(row2-2,row1,-1):
            result[i][col1] = num
            num+=1
            row1+=1
            row2-=1
            col1+=1
            col2-=1
    print(result)
    # return result

solve('data', A)