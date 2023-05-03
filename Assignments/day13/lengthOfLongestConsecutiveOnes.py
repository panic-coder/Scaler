"""
Problem Description
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.


Input Format
The only argument given is string A.

Output Format
Return the length of the longest consecutive 1’s that can be achieved.


Constraints

1 <= length of string <= 1000000
A contains only characters 0 and 1.


For Example

Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7

"""

# A = "111000"
# A = "111011101"
A = "11010110000000000"

# Python 3 program to find length of
# longest consecutive ones by at most
# one swap in a Binary String

# Function to calculate the length
# of the longest consecutive 1's


def solve(self, A):
	s = A
	n = len(A)

	# To count all 1's in the string
	cnt_one = 0

	cnt = 0
	max_cnt = 0

	for i in range(n):
		if (s[i] == '1'):
			cnt_one += 1
			cnt += 1
		else:
			max_cnt = max(max_cnt, cnt)
			cnt = 0

	max_cnt = max(max_cnt, cnt)

	# To store cumulative 1's
	left = [0] * n
	right = [0] * n

	if (s[0] == '1'):
		left[0] = 1

	else:
		left[0] = 0

	if (s[n - 1] == '1'):
		right[n - 1] = 1

	else:
		right[n - 1] = 0

	# Counting cumulative 1's from left
	for i in range(1, n):
		if (s[i] == '1'):
			left[i] = left[i - 1] + 1

		# If 0 then start new cumulative
		# one from that i
		else:
			left[i] = 0

	for i in range(n - 2, -1, -1):

		if (s[i] == '1'):
			right[i] = right[i + 1] + 1

		else:
			right[i] = 0

	for i in range(1, n-1):

		# perform step 3 of the approach
		if (s[i] == '0'):

			# step 3
			sum = left[i - 1] + right[i + 1]

			if (sum < cnt_one):
				max_cnt = max(max_cnt, sum+1)

			else:
				max_cnt = max(max_cnt, sum)
    # print(max_cnt)
	return max_cnt


print(solve('data', A))