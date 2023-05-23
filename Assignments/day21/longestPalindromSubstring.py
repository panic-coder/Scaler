"""

Problem Description
Given a string A of size N, find and return the longest palindromic substring in A.
Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).



Problem Constraints
1 <= N <= 6000



Input Format
First and only argument is a string A.



Output Format
Return a string denoting the longest palindromic substring of string A.



Example Input
Input 1:
A = "aaaabaaa"

Input 2:
A = "abba


Example Output
Output 1:
"aaabaaa"

Output 2:
"abba"


Example Explanation
Explanation 1:
We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".

Explanation 2:
We can see that longest palindromic substring is of length 4 and the string is "abba".


"""

A = 'acicaa'

def solve(self, A):
    mid = 0
    start = 0
    end = 0
    n = len(A)
    largestLength = 0
    pointA = 0
    pointB = 0

    for mid in range(n):
        start = mid
        end = mid
        while(start >= 0 and end < n and A[start] == A[end]):
            start = start - 1
            end = end + 1
        length = end-start-1
        if largestLength < length:
            largestLength = length
            pointA = start + 1
            pointB = end - 1
    
    for mid in range(n):
        start = mid
        end = mid + 1
        while(start >= 0 and end < n and A[start] == A[end]):
            start = start - 1
            end = end + 1
        length = end-start-1
        if largestLength < length:
            largestLength = length
            pointA = start + 1
            pointB = end - 1
    # print(pointA)
    # print(pointB)
    answer = ''
    for i in range(pointA, pointB+1):
        answer = answer + A[i]
        # print(A[i])
    print(answer)


solve('data', A)
