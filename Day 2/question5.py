"""
Given an integer array nums, find three numbers whose product is maximum and return the
maximum product.
Example 1:
Input: nums = [1,2,3]
Output: 6
"""

def productTopThree(sorted_nums):
    result = 1
    for i in range(1,4):
        result = result*sorted_nums[-i]
    print("Product of three biggest numbers in the list are", result)

nums = [9,1,7,11,2,0]
sorted_nums = sorted(nums)
print("the sorted list in ascending order is", sorted_nums)

productTopThree(sorted_nums)

"""INPUT
nums = [9,1,7,11,2,0]
OUTPUT
the sorted list in ascending order is [0, 1, 2, 7, 9, 11]
Product of three biggest numbers in the list are 693
"""
