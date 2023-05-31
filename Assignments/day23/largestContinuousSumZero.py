"""

Problem Description
Given an array A of N integers.

Find the largest continuous sequence in a array which sums to zero.



Problem Constraints
1 <= N <= 106

-107 <= A[i] <= 107



Input Format
Single argument which is an integer array A.



Output Format
Return an array denoting the longest continuous sequence with total sum of zero.

NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.



Example Input
A = [1,2,-2,4,-4]


Example Output
[2,-2,4,-4]


Example Explanation
[2,-2,4,-4] is the longest sequence with total sum of zero.

"""

A = [1,2,-2,4,-4]
def lszero(self, A):
    # hash_map = {}
    # max_len = 0
    # curr_sum = 0
    # for i in range(len(A)):
    #     curr_sum += A[i]
    #     if curr_sum == 0:
    #         max_len = i + 1
    #         print('max_len ', max_len)
    #     if curr_sum in hash_map:
    #         max_len = max(max_len, i - hash_map[curr_sum])
    #         print('max_len ', max_len)
    #     else:
    #         hash_map[curr_sum] = i
    # # return max_len
    # print(max_len)
    # print('hash_map ',hash_map)
    from collections import defaultdict
    N = len(A)
    pre = [None]*N
    curr = 0
    for i in range(N):
        curr += A[i]
        pre[i] = curr
        
    #print pre
        
    seen_table = defaultdict(list)
    seen_table[0]=[-1]
    longest = -1
    indices = None
    for i in range(N):
        s = pre[i]
        seen_table[s].append(i)
        gap = seen_table[s][-1] - seen_table[s][0]
        if gap > longest:
            longest = gap
            indices = (seen_table[s][0]+1,seen_table[s][-1]+1)
    if indices:
        return A[indices[0]:indices[1]]
    else:
        return []


lszero('data', A)