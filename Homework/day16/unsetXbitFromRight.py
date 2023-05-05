"""

Problem Description
Given an integer A. Unset B bits from the right of A in binary.


For eg:-
A = 93, B = 4
A in binary = 1011101
A should become = 1010000 = 80. Therefore return 80.


Problem Constraints
1 <= A <= 1018
1 <= B <= 60


Input Format
The first argument is a single integer A.
The second argument is a single integer B.


Output Format
Return the number with B unset bits from the right.


Example Input
Input 1:-
A = 25
B = 3

Input 2:-
A = 37
B = 3


Example Output
Output 1:-
24

Output 2:-
32


Example Explanation
Explanation 1:-
A = 11001 to 11000

Explantio 2:-
A = 100101 to 100000


Results
1. Change number to binary
2. Set all the values from right to 0 till count B
3. Change binary into decimnal

"""

import math

A = 53
B = 5
def solve(self, A, B):
    print(A)
    n = A
    binaryA = []
    while n>0:
        binaryA.append(n%2)
        n = n//2
    print(binaryA)
    n = len(binaryA)-1
    i = 0
    while(i<B):
        binaryA[i] = 0
        i = i + 1
        # n = n - 1
    binaryA.reverse()
    print(binaryA)
    n = len(binaryA)
    decimal = 0
    i = 0
    while(i < len(binaryA)):
        decimal = decimal + (binaryA[i] * int(math.pow(2,n)))
        i = i + 1
        n = n - 1
    print(int(decimal/2))

solve('data', A, B)