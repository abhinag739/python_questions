#Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
#he can remove just one character at the index in the string, and the remaining characters will occur the same
#number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .

def findMissing(arr, N):
    # create a list of zeroes
    temp = [0] * (N+1)
 
    for i in range(0, N):
        temp[arr[i] - 1] = 1

    print(temp)
 
    for i in range(0, N+1):
        if(temp[i] == 0):
            ans = i + 1
 
    print(ans)




arr = [1, 2, 3, 5]
N = len(arr)
findMissing(arr, N)