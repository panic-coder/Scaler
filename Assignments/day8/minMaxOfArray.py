"""
Problem Description
Write a program to print maximum and minimum elements of the input array A of size N where you have to take integer N and other N elements as input from the user.


Problem Constraints
1 <= N <= 1000
1 <= A <= 1000


Input Format
A single line representing N followed by N integers of the array A

Output Format
A single line containing two space separated integers representing maximum and minimum elements of the input array.


Example Input
Input 1:
5 1 2 3 4 5

Input 2:
4 10 50 40 80


Example Output
Output 1:
5 1

Output 2:
80 10

"""

A = input().split()
largest = -10e9;
smallest = 10e9
i = 1
n = len(A)
outputArray = []
if n > 0:
    while i < n:
        if (largest < int(A[i])):
            largest = int(A[i])
        if (smallest > int(A[i])):
            smallest = int(A[i])
        i = i + 1
    outputArray.append(largest)
    outputArray.append(smallest)
    for i in range(0, len(outputArray)):
        if i == len(outputArray)-1:
            print(outputArray[i], end = "")
        else:
            print(outputArray[i], end = " ")