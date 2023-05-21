"""

Problem Description
You are given a string A of size N consisting of lowercase alphabets.
You can change at most B characters in the given string to any other lowercase alphabet such that the number of distinct characters in the string is minimized.
Find the minimum number of distinct characters in the resulting string.



Problem Constraints
1 <= N <= 100000
0 <= B < N



Input Format
The first argument is a string A.
The second argument is an integer B.



Output Format
Return an integer denoting the minimum number of distinct characters in the string.



Example Input
A = "abcabbccd"
B = 3



Example Output
2



Example Explanation
We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
So the minimum number of distinct character will be 2.

"""

# A = "abcabbccd"
# A = "hq"
# A = "ircvscxggbwkfnqd"
A = "umeaylnlfd"
B = 1
def solve(self, A, B):
    distinctCount = 1
    dict = {}
    count, itm = 0, ''
    array = []
    for item in reversed(A):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count :
            count, itm = dict[item], item
            # array.append(count)
    print(dict)
    for i in dict.values():
        array.append(i)
    array.sort()
    answer = len(array)
    if answer == 1:
        return 1
    # print(array)
    if B>0:
        # print(answer)
        for i in array:
            # print(i)
            # print(B)
            if B >= i:
                B = B - i
                answer = answer - 1
            else:
                break
        
    return max(answer, 1)
    
    




solve('data', A, B)