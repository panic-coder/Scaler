"""
Problem Description
Write a program to input an integer N from user and print hollow diamond star pattern series of N lines.
See example for clarifications over the pattern.


Problem Constraints
1 <= N <= 1000


Input Format
First line is an integer N

Output Format
N lines conatining only char '*' as per the question.


Example Input
Input 1:
4

Input 2:
6


Example Output
Output 1:
********
***  ***
**    **
*      *
*      *
**    **
***  ***
********

Output 2:
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************

"""

def solve():
    rows = int(input("Enter the size "))
    x = 1
    y = 1
    for x in range(1, rows+1):
        # Print star
        for y in range(x, rows+1):
            print("*",end="")
        # Print spaces
        y = 1
        while(y <= (2*x)-2):
            print(" ",end="")
            y = y + 1
        # Print star
        for y in range(x, rows+1):
            print("*",end="")
        # Print new line
        print()
    
    for x in range(1,rows+1):
        # Print star
        y = 1
        while(y <= x):
            print("*",end="")
            y = y + 1
        # Print spaces
        y = ((2*x)-2)
        while(y<((2*rows)-2)):
            print(" ",end="")
            y = y + 1
        y = 1
        # Print star
        while(y <= x):
            print("*",end="")
            y = y + 1
        # Print new line
        print()

solve()