"""

Problem Description
Find the number of occurrences of bob in string A consisting of lowercase English alphabets.



Problem Constraints
1 <= |A| <= 1000


Input Format
The first and only argument contains the string A, consisting of lowercase English alphabets.


Output Format
Return an integer containing the answer.


Example Input
Input 1:
  "abobc"

Input 2:
  "bobob"


Example Output
Output 1:
  1

Output 2:

  2


Example Explanation
Explanation 1:
  The only occurrence is at second position.

Explanation 2:
  Bob occures at first and third position.

"""
# A = "abobc"
A = "bobob"
def solve(self, A):
    count = 0
    word = 'bob'
    startIndex = 0
    endIndex = startIndex + 2
    while(endIndex < len(A)):
        currentWord = A[startIndex] + A[startIndex+1] + A[endIndex]
        print(currentWord)
        if currentWord == word:
            count = count + 1
        startIndex = startIndex + 1
        endIndex = endIndex + 1
    print(count)
    

solve('data', A)
