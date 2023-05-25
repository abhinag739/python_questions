def min_count(array1, n):
    total_sums = 0
    i,j = 0,n-1
    while i<j:
        if array1[i] == array1[j]:
            i += 1
            j -= 1
        elif array1[i] > array1[j]:
            j -= 1
            array1[j] += array1[j+1]
            total_sums += 1
        else:
            i += 1
            array1[i] += array1[j+1]
            total_sums += 1

    print("the palindrome is", array1)    
    return total_sums



array1 = [1,9,4,1,2,1]
n = len(array1)


if (array1 == array1.reverse):
    print("its palindrome")
else:
    print("not palindrome")
    print("Number of additions to make array palindrome is", min_count(array1, n))
