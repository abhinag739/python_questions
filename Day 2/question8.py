"""
You are given an integer array nums and an integer k.
In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i]
to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at
most once for each index i.
The score of nums is the difference between the maximum and minimum elements in nums.
Return the minimum score of nums after applying the mentioned operation at most once for
each index in it.
Example 1:
Input: nums = [1], k = 0
Output: 0
"""



def smallestRangeI(nums, k):
    sorted_nums=sorted(nums)
    low = sorted_nums[0] + k
    high = sorted_nums[len(sorted_nums)-1] - k
    result = high - low
    if(result<0):
        print(0)
    else:
        print(result)


nums = [1]
k=3
smallestRangeI(nums,k)

"""
INPUT
nums = [0,10,4]
OUTPUT
4

INPUT 2
nums = [1]
0
"""