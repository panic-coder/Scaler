"""

Problem Description
You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Note: Read-only array means that the input array should not be modified in the process of solving the problem



Problem Constraints
1 <= N <= 7*105
1 <= A[i] <= 109


Input Format
The only argument is an integer array A.


Output Format
Return an integer.


Example Input
Input 1:
[1 2 3 1 1]
Input 2:
[1 2 3]


Example Output
Output 1:
1
Output 2:
-1


Example Explanation
Explanation 1:
1 occurs 3 times which is more than 5/3 times.
Explanation 2:
No element occurs more than 3 / 3 = 1 times in the array.

"""

A = [1, 2, 3, 5, 4]
def repeatedNumber(self, A):
    dict = {}
    count, itm = 0, ''
    for item in reversed(A):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count :
            count, itm = dict[item], item
    print("🚀 ~ file: 3RepeatedNumber.py:56 ~ count:", dict)
    print("🚀 ~ file: 3RepeatedNumber.py:58 ~ len(A)/3:", len(A)/3)
    if count > len(A)/3:
        print(itm)
    else:
        print(-1)
    # return(itm)

repeatedNumber('data', A)

