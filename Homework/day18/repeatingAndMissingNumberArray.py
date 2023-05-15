"""



"""
A = [3, 1, 2, 5, 3]
def solve(self, A):
    n = len(A)
    temp = [0] * n  # Creating temp array of size n with initial values as 0.
    repeatingNumber = -1
    missingNumber = -1
 
    for i in range(n):
        temp[A[i] - 1] += 1
        if temp[A[i] - 1] > 1:
            repeatingNumber = A[i]
    for i in range(n):
        if temp[i] == 0:
            missingNumber = i + 1
            break
 
    print("The repeating number is", repeatingNumber, ".")
    print("The missing number is", missingNumber, ".")

solve('data', A)