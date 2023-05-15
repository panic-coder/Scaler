"""

Problem Description
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.



Problem Constraints
1 <= N <= 5*105
1 <= num[i] <= 109


Input Format
Only argument is an integer array.


Output Format
Return an integer.


Example Input
Input 1:
[2, 1, 2]

Input 2:
[1, 1, 1]


Example Output
Input 1:
2

Input 2:
1


Example Explanation
For Input 1:
2 occurs 2 times which is greater than 3/2.

For Input 2:
1 is the only element in the array, so it is majority

"""
A = [2, 1, 2]
def majorityElement(self, A):
    dict = {}
    count, itm = 0, ''
    for item in reversed(A):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count :
            count, itm = dict[item], item
    print(itm)
    # return(itm)


majorityElement('data', A)