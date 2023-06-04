"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.
Example 1:
Input: nums = [1,2,2,3]
Output: true
"""

def check(arr):
    N = len(arr)
    inc = True
    dec = True
     
    # Loop to check if array is increasing
    for i in range(0, N-1):
       
        # To check if array is not increasing
        if arr[i] > arr[i+1]:
            inc = False
 
    # Loop to check if array is decreasing
    for i in range(0, N-1):
       
       # To check if array is not decreasing
        if arr[i] < arr[i+1]:
            dec = False
 
    # Pick one whether inc or dec
    return inc or dec



nums = [1,2,2,3]
print(check(nums))

"""
INPUT
nums = [1,2,1,2,3]

OUTPUT
False (not monotonic)

INPUT 2
nums = [1,2,2,3]
OUTPUT
True (monotonic)
"""