"""

You are given a string S, and you have to find all the amazing substrings of S.

An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input

Only argument given is string S.
Output

Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.
Constraints

1 <= length(S) <= 1e6
S can have special characters

Example
Input
    ABEC

Output
    6

Explanation
    Amazing substrings of given string are :
    1. A
    2. AB
    3. ABE
    4. ABEC
    5. E
    6. EC
    here number of substrings are 6 and 6 % 10003 = 6.

"""

A = 'ABEC'
def solve(self, A):
    subArrayCount = 0
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    for i in range(0, len(A)):
         if(A[i].startswith(vowels)):
              subArrayCount = subArrayCount + (len(A) - i)
    print(subArrayCount%10003)

    # outputArray = []
    # string = ''
    # for i in range(0,len(A)):
    #     for j in range(i,len(A)):
    #         for k in range(i,j+1):
    #             string = string + A[k]
    #         outputArray.append(string)
    #         string = ''
    # # print(outputArray)
    # subarrayWithVowels = []
    # vowels = ('a','e','i','o','u','A','E','I','O','U')
    # for i in range(len(outputArray)):
    #     if(outputArray[i].startswith(vowels)):
    #         subarrayWithVowels.append(outputArray[i])
    # print(subarrayWithVowels)
    # print(len(subarrayWithVowels)%10003)

solve('data', A)

