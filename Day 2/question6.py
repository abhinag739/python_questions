"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.
You must write an algorithm with O(log n) runtime complexity.
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""


nums = [-1,0,3,5,9,12]
sorted_nums = sorted(nums)
target = int(input("enter the number to be searched "))

if target in sorted_nums:
    print("the target", target, " exists in position ", sorted_nums.index(target))
else:
    print(-1)



"""INPUT
nums = [-1,0,3,5,9,12]
Input 12

OUTPUT
enter the number to be searched 12
the target 12  exists in position  5

INPUT 2
nums = [-1,0,3,5,9,12]
Input 99

OUTPUT
-1
"""