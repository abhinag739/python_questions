"""

    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

    **Example 1:**
    Input: nums = [1,3,5,6], target = 5

    Output: 2



"""

def returnIndex(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return(i)


nums = [1,0,4,5,1,8]
target = 4

print("the target variable", target," is found at position ", returnIndex(nums,target))


"""INPUT
nums = [1,0,4,5,1,8]
target = 8

OUTPUT
the target variable 8  is found at position  5

"""