"""
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

    Note that you must do this in-place without making a copy of the array.

    **Example 1:**
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]


"""

def moveToEnd(nums):

    for i in nums[:]:
        if i == 0:
            nums.remove(i)
            nums.append(0)

    return nums

list1 = [0,1,0,3,0,0,0,7,1]
nums = moveToEnd(list1)

print(nums)


"""
INPUT
list1 = [0,1,0,3,0,0,0,7,1]

OUTPUT
[1, 3, 7, 1, 0, 0, 0, 0, 0]
"""
