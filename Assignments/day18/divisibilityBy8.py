"""

Problem Description
You are given a number A in the form of a string. Check if the number is divisible by eight or not.
Return 1 if it is divisible by eight else, return 0.


Problem Constraints
1 <= length of the String <= 100000
'0' <= A[i] <= '9'


Input Format
The only argument given is a string A.


Output Format
Return 1 if it is divisible by eight else return 0.


Example Input
Input 1:
A = "16"

Input 2:
A = "123"


Example Output
Output 1:
1

Output 2:
0


Example Explanation
Explanation 1:
16 = 8 * 2

Explanation 2:
123 = 15 * 8 + 3

"""
A = "1645400"
def solve(self, A):
    rem = 0
    if len(A) <= 3:
        rem = int(A)%8
    else:
        # print(A[len(A)-1])
        # print(A[len(A)-2])
        # print(A[len(A)-3])
        number = int(A[len(A)-3] + A[len(A)-2] + A[len(A)-1])
        # print(number)
        if number == 000:
            rem = 0
        else:
            rem = int(A)%8
    if rem == 0:
        print(1)
        # return 1
    else:
        print(0)
        return 0
    

solve('data', A)