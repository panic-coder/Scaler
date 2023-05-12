"""

Problem Description
Given an integer A representing a year, Return 1 if it is a leap year else, return 0.

A year is a leap year if the following conditions are satisfied:

The year is multiple of 400.
or the year is multiple of 4 and not multiple of 100.

Problem Constraints
1 <= A <= 109



Input Format
First and only argument is an integer A



Output Format
Return 1 if it is a leap year else return 0



Example Input
Input 1
A = 2020

Input 2:
A = 1999


Example Output
Output 1
1

Output 2:
0


Example Explanation

Explanation 1
2020 is a leap year.

Explanation 2:
1999 is not a leap year.

"""

A = 1999
def solve(self, A):
    if (A % 400 == 0) and (A % 100 == 0):
        print("{0} is a leap year".format(A))
    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (A % 4 ==0) and (A % 100 != 0):
        print("{0} is a leap year".format(A))

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        print("{0} is not a leap year".format(A))

solve('data', A)