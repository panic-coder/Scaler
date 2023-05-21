"""

Problem Description
Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:

Concatenate the string with itself.
Delete all the uppercase letters.
Replace each vowel with '#'.
You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.

NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.



Problem Constraints
1<=N<=100000


Input Format
First argument is a string A of size N.



Output Format
Return the resultant string.



Example Input
Input 1:
A="aeiOUz"

Input 2:
A="AbcaZeoB"


Example Output
Output 1:
"###z###z"

Output 2:
"bc###bc###"


Example Explanation
Explanatino 1:
First concatenate the string with itself so string A becomes "aeiOUzaeiOUz".
Delete all the uppercase letters so string A becomes "aeizaeiz".
Now replace vowel with '#', A becomes "###z###z".

Explanatino 2:
First concatenate the string with itself so string A becomes "AbcaZeoBAbcaZeoB".
Delete all the uppercase letters so string A becomes "bcaeobcaeo".
Now replace vowel with '#', A becomes "bc###bc###".

"""

A="aeiOUz"

def solve(self, A):
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    array = []
    string = ''
    for i in range(len(A)):
        # print(A[i].isupper())
        if A[i].isupper() == False:
            array.append(A[i])
    # print(array)
    for i in range(len(array)):
        # print(array[i].startswith(vowels))
        if(array[i].startswith(vowels)):
            string = string + '#'
        else:
            string = string + array[i]
    print(string+string)
    # string = A
    # print(string)

    # for i in range(len(string)):
    #     # print(string[i].isupper())
    #     if string[i].isupper():
    #          string = string.replace(string[i], "")
    #     if(string[i].startswith(vowels)):
    #         string = string.replace(string[i], "#")
    # print(string)



solve('data', A)