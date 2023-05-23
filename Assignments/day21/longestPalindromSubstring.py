"""



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
