"""

    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least 
    
    significant in left-to-right order. The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

    **Example 1:**
    Input: digits = [1,2,3]
    Output: [1,2,4]

"""

def plusOne(nums):
    nums_length = len(nums)
    i = nums_length - 1

    while nums[i] == 9 and i >= 0:
            i -= 1

    if i == -1:
                results = [0]*(nums_length + 1)
                results[0] = 1
                return results

    results = [0]*(nums_length)
        
    results[i] = nums[i] + 1

    for j in range(i-1, -1, -1):
            results[j] = nums[j]

    return results


nums = [1,2,3]
print(plusOne(nums))


"""
INPUT
Nums = [1,2,3]

OUTPUT
[1, 2, 4]
"""