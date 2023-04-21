"""
Problem Description
Given an integer A, you have to tell whether it is a prime number or not.
A prime number is a natural number greater than 1 which is divisible only by 1 and itself.


Problem Constraints
1 <= A <= 106


Input Format
First and only line of the input contains a single integer A.

Output Format
Print YES if A is a prime, else print NO.


Example Input

Input 1:
 3 

Input 2:
 4 


Example Output

Output 1:
 YES 

Output 2:
 NO 


Example Explanation

Explanation 1:
 3 is a prime number as it is only divisible by 1 and 3.

Explanation 2:
 4 is not a prime number as it is divisible by 2.

"""

import math 
number = int(input())
sqrt = round(number ** 0.5)
sqrt = math.floor(sqrt)
print(sqrt)
count = 0;
for index in range(2,sqrt+1):
    print(number%index)
    if (number%index) == 0:
        count = count+1
        # print("NO")
        # break
    # else:
        # print("YES")
        # break
if(count>0):
    print("NO")
    # break
else:
    print("YES")
    # break
