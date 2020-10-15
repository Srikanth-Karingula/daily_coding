# Given a non-negative integer n, find a number r such that r * r = n and round down to the nearest integer.

# Can you implement this without using the built-in square root?

def guessTheRoot(n):
    iteration = 0
    start = 0
    end = n
    mid = 0
    ans = 0
    while start <= end:
        iteration += 1
        mid = (start+end)//2
        midSqr = mid * mid
        if midSqr == n:
            print(iteration)
            return mid
        elif midSqr < n:
            start = mid+1
            ans = mid
        else:
            end = mid-1
    print(iteration)
    return ans


print('Root is : ', guessTheRoot(2000))


# https://binarysearch.com/room/Binary-Search-ry1W19WGTw
