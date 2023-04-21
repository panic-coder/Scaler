"""
Problem Description
You are given an integer array A.
Decide whether it is possible to divide the array into one or more subarrays of even length such that the first and last element of all subarrays will be even.
Return "YES" if it is possible; otherwise, return "NO" (without quotes).


Problem Constraints
1 <= |A|, A[i] <= 106


Input Format
The first and the only input argument is an integer array, A.

Output Format
Return a string "YES" or "NO" denoting the answer.


Example Input
Input 1:
 A = [2, 4, 8, 6]

Input 2:
 A = [2, 4, 8, 7, 6]


Example Output
Output 1:
 "YES"

Output 2:
 "NO"


Example Explanation
Explanation 1:
 We can divide A into [2, 4] and [8, 6].

Explanation 2:
 There is no way to divide the array into even length subarrays.

"""

# A = [2, 4, 8, 6]
# A = [2, 4, 8, 7, 6]
# A = [ 654, 50, 694, 750, 712, 275, 736, 146, 279, 816, 707, 396, 406, 589, 370, 742, 840, 290, 505, 23, 249, 447, 618, 80, 968, 189, 600, 662, 91, 604, 575, 689, 72, 196, 475, 198, 850, 844, 361, 419, 617, 911, 268, 628, 408, 404, 477, 921, 478, 806, 204, 637, 403, 911, 589, 529, 867, 584, 768, 257, 437, 380, 698, 452, 368, 97, 977, 582, 775, 103 ]
A = [ 978, 847, 95, 729, 778, 586, 188, 782, 813, 870, 871, 940, 312, 693, 580, 101, 760, 837, 564, 633, 680, 155, 241, 374, 682, 290, 850, 601, 433, 922, 773, 959, 530, 290, 990, 50, 516, 409, 868, 131, 664, 851, 721, 880, 20, 450, 745, 387, 787, 823, 392, 242, 674, 347, 65, 135, 819, 324, 651, 678, 139, 940 ]

def solve(self, A):
    if (len(A)%2!=0) or (A[0]%2!=0) or (A[len(A)-1]%2!=0):
        print(0)
        # return "NO"
    else:
        print(1)
        # return "YES"

solve('data', A)