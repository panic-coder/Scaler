"""

Problem Description
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.
The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".



Problem Constraints
0 <= sum of length of all strings <= 1000000



Input Format
The only argument given is an array of strings A.



Output Format
Return the longest common prefix of all strings in A.



Example Input
Input 1:
A = ["abcdefgh", "aefghijk", "abcefgh"]

Input 2:
A = ["abab", "ab", "abcd"];


Example Output
Output 1:
"a"

Output 2:
"ab"


Example Explanation
Explanation 1:
Longest common prefix of all the strings is "a".

Explanation 2:
Longest common prefix of all the strings is "ab".

"""
# A = ["abcdefgh", "abefghijk", "abcefgh", "abc"]
# A = ["ABCD"]
A = ["aaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
def longestCommonPrefix(self, A):
    shortestStringLength = len(A[0])
    # shortestIndex = 0
    shortestString = A[0]
    answer = ''
    # print(shortestStringLength)
    print(len(A))
    if len(A) == 1:
        print(A[0])
        # break
    for i in A:
        # print(len(i))
        if(len(i) < shortestStringLength):
            shortestStringLength = len(i)
            # shortestIndex = i
            shortestString = i
    print()
    print(shortestString)
    print(shortestStringLength)
    # print(A)
    
    for i in range(0, shortestStringLength):
        isQualified = True
        ch = shortestString[i]
        for j in range(0, len(A)):
            checkString = A[j][i]
            if checkString != ch:
                isQualified = False
                break
        if isQualified:
            answer = answer + ch
        else:
            print(answer)
            break
    print(answer)
            


longestCommonPrefix('data', A)