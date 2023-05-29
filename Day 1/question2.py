"""
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are 
    not equal to val.

    Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    - Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    - Return k.

Example :
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

"""

class RemoveNum:
    def removeNum(self, nums, val: int):
        # Counter for keeping track of elements other than val
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                # If the element is found, shift digits left and append 0 in end
                nums.pop(i) and nums.append(0)
                count += 1
        
        return(count, nums)


input = [3,2,2,1,3]
val = 3
re = RemoveNum()
print("the count and output after removing the value", val, " is ", re.removeNum(input, val))


"""INPUT
input = [3,2,2,1,3]
val = 3

OUTPUT
the count and output after removing the value 3  is  (2, [2, 2, 1, 0, 0])
"""
