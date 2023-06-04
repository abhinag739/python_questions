"""

We define a harmonious array as an array where the difference between its maximum value
and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence
among all its possible subsequences.
A subsequence of an array is a sequence that can be derived from the array by deleting some
or no elements without changing the order of the remaining elements.
Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5

"""

def harmoniousSeq(nums):
    sorted_arr = sorted(nums)
    print(sorted_arr)
    left = 0; right = 1
    result = 0
    while(right < len(sorted_arr)):
        diff = sorted_arr[right] - sorted_arr[left]
        if(diff == 1):
            result = max(result, right - left + 1)
        if(diff <= 1):
            right += 1
        else:
            left += 1
    
    print(result)

nums = [1,3,2,2,5,2,3,7]
n = len(nums)

harmoniousSeq(nums)


"""INPUT
nums = [1,3,2,2,5,2,3,7]
OUTPUT
5
"""