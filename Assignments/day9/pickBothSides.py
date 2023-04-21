"""
Problem Description
You are given an integer array A of size N.
You have to pick B elements in total. Some (possibly 0) elements from left end of array A and some (possibly 0) from the right end of array A to get the maximum sum.
Find and return this maximum possible sum.

NOTE: Suppose B = 4, and array A contains 10 elements, then
You can pick the first four elements or can pick the last four elements, or can pick 1 from front and 3 from the back, etc. You need to return the maximum possible sum of elements you can pick.


Problem Constraints
1 <= N <= 105
1 <= B <= N
-103 <= A[i] <= 103


Input Format
First argument is an integer array A.
Second argument is an integer B.

Output Format
Return an integer denoting the maximum possible sum of elements you picked.


Example Input
Input 1:
 A = [5, -2, 3 , 1, 2]
 B = 3

Input 2:
 A = [1, 2]
 B = 1


Example Output
Output 1:
 8

Output 2:
 2


Example Explanation
Explanation 1:
Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8

Explanation 2:
Pick element 2 from end as this is the maximum we can get

"""

# A = [5, -2, 3 , 1, 2]
# B = 3
A = [-533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35]
B = 48
def maxSum(A, B, start, end, max_sum):
     
    # Base case
    if (B == 0):
        return max_sum
 
    # PicB the start index
    max_sum_start = max_sum + A[start]
 
    # PicB the end index
    max_sum_end = max_sum + A[end]
 
    # Recursive function call
    ans = max(maxSum(A,  B - 1, start + 1,
                     end, max_sum_start),
          maxSum(A, B - 1, start,
                     end - 1, max_sum_end))
 
    # Return the final answer
    return ans
 
# Function to find the maximized sum
def maximizeSum(A, B):
    n = len(A)
    max_sum = 0
    start = 0
    end = n - 1
 
    print(maxSum(A, B, start, end, max_sum))

maximizeSum(A, B)