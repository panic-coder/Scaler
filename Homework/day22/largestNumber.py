"""

Problem Description
Given an array A of non-negative integers, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.



Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*109



Input Format
The first argument is an array of integers.



Output Format
Return a string representing the largest number.



Example Input
Input 1:
 A = [3, 30, 34, 5, 9]

Input 2:
 A = [2, 3, 9, 0]


Example Output
Output 1:
 "9534330"

Output 2:
 "9320"


Example Explanation
Explanation 1:
Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.

Explanation 2:
Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320.

"""

A = [3, 30, 34, 5, 9]
from itertools import permutations

def largestNumber(self, A):
    print(A)
    # lst = []
    # for i in permutations(A, len(A)):
    #     # provides all permutations of the list values,
    #     # store them in list to find max
    #     lst.append("".join(map(str,i)))
    # # return max(lst)
    # # print(lst)
    # print(max(lst))
    # array = A
    # if len(array)==1: 
    #     return str(array[0])
    # for i in range(len(array)):
    #     array[i]=str(array[i])
    # # [54,546,548,60]=>['54','546','548','60']
    # #Second, we find the largest element by swapping technique.
    # for i in range(len(array)):
    #     for j in range(1+i,len(array)):
    #         if array[j]+array[i]>array[i]+array[j]:
    #             array[i],array[j]=array[j],array[i]
    # #['60', '548', '546', '54']
    # #Refer JOIN function in Python
    # result=''.join(array)
    # print(result)
    # if(result=='0'*len(result)):
    #     return '0'
    # else:
    #     return result
    import functools

    def myCompare(x, y):
    
        xy = x
        yx = y
    
        # Count length of x and y
        countx = 0
        county = 0
    
        # Count length of X
        while (x > 0):
            countx += 1
            x //= 10
    
        # Count length of Y
        while (y > 0):
            county += 1
            y //= 10
    
        x = xy
        y = yx
    
        while (countx):
            countx -= 1
            yx *= 10
    
        while (county):
            county -= 1
            xy *= 10
    
        # Append x to y
        yx += x
    
        # Append y to x
        xy += y
    
        return 1 if xy > yx else -1

    arr = A
    arr.sort(key=functools.cmp_to_key(myCompare))
    arr.reverse()
 
    # print("".join(map(str, arr)))

    result = ("".join(map(str, arr)))
    if(result=='0'*len(result)):
        return '0'
    else:
        return str(result)



largestNumber('data', A)